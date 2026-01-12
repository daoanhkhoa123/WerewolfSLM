from roles import Role
from engine.state_engine.common.player import PlayerEntity
from typing import Any
from engine.ultils.event import Event, ConEnum
from src.engine.ultils.con_enum import ConEnum, con_auto
from collections import deque
from dataclasses import dataclass
from src.engine.player_entity_manager import system

@dataclass
class ChatMessage:
    author: PlayerEntity
    message: str

    def __str__(self):
        return f"{self.author.name}: {self.message}"

class ChatEnum(ConEnum):
    CHT_SEND = con_auto()

class ChatEvent(Event):
    def __init__(self, author: PlayerEntity, message:str) -> None:
        super().__init__(author, system, ChatEnum.CHT_SEND)
        self.messaage = message

class ChatEngne:
    def __init__(self, max_size: int = 8) -> None:
        self.chat_queue = deque(maxlen=max_size)

    def chat(self, author: PlayerEntity, msg:str):
        self.chat_queue.append(ChatMessage(author, msg))

    def clear(self):
        self.chat_queue.clear()

    def show(self):
        return "\n".join(str(chat) for chat in self.chat_queue)
            