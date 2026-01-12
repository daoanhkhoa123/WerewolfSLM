from typing import final
from enum import IntEnum, auto
from dataclasses import dataclass
from src.engine.event_engine.event_context import Context

# should not be extended
@final
class GameTimeEnum(IntEnum):
    DAY = auto()
    NIGHT = auto()

@dataclass
class GameContext(Context):
    time: GameTimeEnum