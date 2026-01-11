from typing import Dict, Sequence, final, List
from src.engine.state_engine.common.player import PlayerEntity
from src.engine.state_engine.common.state import PlayerStateEnum
from src.role import RoleEnum, build_role
import random
from enum import auto, IntEnum

# should not be extended
@final
class GameTimeEnum(IntEnum):
    DAY = auto()
    NIGHT = auto()
    LYNCHING = auto()

class PlayerManager:
    def __init__(self, names: Sequence[str], register_roles: Dict[RoleEnum, int]) -> None:
        if len(names) != sum(x for x in register_roles.values()):
            raise ValueError("Number of names must match total registered roles")
         
        self._names = names
        self._register_roles = register_roles
        self._players: Dict[RoleEnum, List[PlayerEntity]] = {}

    @property
    def players(self):
        return self._players

    def build_players(self, shuffle:bool = True):
        role_pool = list()
        for enum, count in self._register_roles.items():
            role_pool.extend([enum] * count)
        
        if shuffle:
            random.shuffle(role_pool)

        for enum, name in zip(role_pool, self._names):
            if enum not in self._players:
                self._players[enum] = [PlayerEntity(name, build_role(enum))]
                continue
            self._players[enum].append(PlayerEntity(name, build_role(enum)))


class GameplayEngine(PlayerManager):
    def __init__(self, names: Sequence[str], register_roles: Dict[RoleEnum, int]) -> None:
        super().__init__(names, register_roles)

        self._day_count = 0
        self._current_time: GameTimeEnum = GameTimeEnum.NIGHT
    
    @property
    def day_count(self) -> int:
        return self._day_count
    
    def next_time(self, time:GameTimeEnum):
        if time == GameTimeEnum.NIGHT:
            self._current_time = GameTimeEnum.DAY
        
        if time == GameTimeEnum.DAY:
            self._current_time = GameTimeEnum.NIGHT
        
        raise ValueError(f"Invalid time: Got {time}; Expected from {GameTimeEnum}")
    
    def get_all_alives(self, role_enum: RoleEnum):
        for player in self.players[role_enum]:
            if player.state != PlayerStateEnum.DEAD:
                yield player

    def night(self):
        for role_enum in RoleEnum:
            for player in self.get_all_alives(role_enum):
