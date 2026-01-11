from typing import Dict, Sequence, final, List
from src.engine.state_engine.common.player import PlayerEntity
from src.role import RoleEnum, build_role
import random
from enum import auto, IntEnum
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    score: int
    controller: Controller


class UserRepository:
    def save()

class UserEngine:
    def __init__(self, names:Sequence[str]) -> None:
        self._player_registry = {}