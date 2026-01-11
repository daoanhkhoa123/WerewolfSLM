from roles import Role
from engine.state_engine.common.player import PlayerEntity
from typing import Any, Iterable
from engine.ultils.event import Event, ConEnum
from src.engine.ultils.con_enum import ConEnum, con_auto
from collections import deque
from dataclasses import dataclass

class VoteEnum(ConEnum):
    VOT_SEND = con_auto()

class VoteEvent(Event):
    def __init__(self, author: PlayerEntity, target: PlayerEntity) -> None:
        super().__init__(author, target, VoteEnum.VOT_SEND)

class VoteEngine:
    def __init__(self, candidates:Iterable[Any]) -> None:
        self.ballot = {c:0 for c in candidates}

    def vote(self, target: Any):
        self.ballot[target] += 1

    def get_winner(self):
        return max(self.ballot.keys(), key=lambda c: self.ballot[c])
    
    def clear(self):
        for c in self.ballot:
            self.ballot[c] = 0

