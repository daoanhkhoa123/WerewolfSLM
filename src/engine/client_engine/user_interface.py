from typing import Any, Type, Sequence, Dict, NewType, List, Union, Optional
from src.engine.event_engine.message_broker import MessageKeyT, Receiver
from dataclasses import dataclass
from src.engine.game_engine import GameTimeEnum
from src.engine.state_engine.common.state import PlayerStateEnum
from src.role import RoleEnum
from src.engine.state_engine.common.action import ActionEnum
from src.engine.event_engine.event_context import Context

@dataclass
class PlayerContext(Context):
    name: str
    state: PlayerStateEnum
    
@dataclass
class GameContext(Context):
    time: GameTimeEnum

@dataclass
class SelfContext(Context):
    role: RoleEnum

class UserInterface(Receiver):
    def __init__(self, name:str) -> None:
        self._name = name   # id for an instance
        self._player_context:Dict[str, PlayerStateEnum] = {}
        self._game_context: Optional[GameTimeEnum] = None
        self._self_context: Optional[RoleEnum] = None

    @property
    def player_context(self) -> Dict[str, PlayerStateEnum]:
        return self._player_context

    @property
    def game_context(self) -> GameTimeEnum:
        if self._game_context is None:
            raise ValueError("Game context has not been set yet.")
        return self._game_context

    @property
    def self_context(self) -> RoleEnum:
        if self._self_context is None:
            raise ValueError("Self context has not been set yet.")
        return self._self_context

    @property
    def name(self):
        return self._name   

    def receive(self, key: MessageKeyT, value: Union[PlayerContext, GameContext, SelfContext]) -> bool:
        if key == PlayerContext.cls_name:
            self._player_context[value.name] = value.state # type: ignore

        if key == GameContext.cls_name:
            self.game_context = value.time # type: ignore

        if key == SelfContext.cls_name:
            self.self_context = value.role # type: ignore

        return True

    def show(self):
        ...