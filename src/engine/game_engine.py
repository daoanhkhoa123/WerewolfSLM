from typing import Dict, Sequence, final, List, Iterator, MutableSequence
from src.engine.state_engine.common.player import PlayerEntity
from src.engine.state_engine.common.state import PlayerStateEnum
from dataclasses import dataclass
from src.role import RoleEnum, build_role
import random
from enum import auto, IntEnum

# should not be extended
@final
class GameTimeEnum(IntEnum):
    DAY = auto()
    NIGHT = auto()
    LYNCHING = auto()

@dataclass
class GameSetting:
    names: Sequence[str]
    register_roles: Dict[RoleEnum, int]

class PlayerEntityManager:
    def __init__(self, game_setting: GameSetting) -> None:

        self._names = game_setting.names
        self._register_roles = game_setting.register_roles
        self._sorted_roleenum = sorted(game_setting.register_roles.keys())
        self._name_entity_map: Dict[str, PlayerEntity] = {n: PlayerEntity(n) for n in game_setting.names}
        self._role_names_map: Dict[RoleEnum, List[str]] = {}

        if len(self._name_entity_map) != len(game_setting.names):
            raise ValueError(
                "Duplicate player names detected in game_setting.names"
            )

        if len(game_setting.names) != sum(x for x in game_setting.register_roles.values()):
            raise ValueError("Number of names must match total registered roles")
    
    @property
    def names(self) -> Sequence[str]:
        return self._names

    @property
    def register_roles(self) -> Dict[RoleEnum, int]:
        return self._register_roles

    @property
    def name_entity_map(self) -> Dict[str, PlayerEntity]:
        return self._name_entity_map

    @property
    def role_names_map(self) -> Dict[RoleEnum, List[str]]:
        return self._role_names_map

    @property
    def sorted_roles(self):
        return self._sorted_roleenum

    def get_players_by_role(self, roleenum:RoleEnum, only_alive: bool = True) -> Iterator[PlayerEntity]:
            for name in self.role_names_map[roleenum]:
                if only_alive and self.name_entity_map[name].state == PlayerStateEnum.DEAD:
                    continue
                yield self.name_entity_map[name]

    def get_players(self, only_alive: bool = True) -> Iterator[PlayerEntity]:
        for roleenum in self.sorted_roles:
            yield from self.get_players_by_role(roleenum, only_alive)

    def _get_role_pool(self) -> MutableSequence[RoleEnum]:
        role_pool = list()
        for enum, count in self._register_roles.items():
            role_pool.extend([enum] * count)

        return role_pool

    def build_role_names_map(self, shuffle:bool = True) -> None:
        role_pool = self._get_role_pool()
        
        if shuffle:
            random.shuffle(role_pool)

        dicc:Dict[RoleEnum, List[str]] = dict()
        for role, name in zip(role_pool, self.names):
            if role not in dicc:
                dicc[role] = list()

            dicc[role].append(name)

        self._role_names_map = dicc