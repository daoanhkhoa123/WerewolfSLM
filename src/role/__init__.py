from enum import IntEnum, auto
from src.engine.state_engine.common.role import Role, RoleTeam
from src.role.guard import GuardRole
from src.role.seer import SeerRole
from src.role.villager import VillagerRole
from src.role.wolf import WolfRole

__all__ = ["RoleEnum", "build_role", "get_role_name"]

class RoleEnum(IntEnum):
    VILLAGER = auto()
    WOLF = auto()
    GUARD = auto()
    SEER = auto()

from typing import Dict, Type

ROLE_FACTORY: Dict[RoleEnum, Type[Role]] = {
    RoleEnum.VILLAGER: VillagerRole,
    RoleEnum.WOLF: WolfRole,
    RoleEnum.GUARD: GuardRole,
    RoleEnum.SEER: SeerRole,
}

def build_role(enum: RoleEnum, *args, **kwargs) -> Role:
    role_cls = ROLE_FACTORY.get(enum)
    if role_cls is None:
        raise ValueError(f"Unregistered RoleEnum: {enum}")
    return role_cls(*args, **kwargs)

def get_role_name(enum: RoleEnum) -> str:
    role_cls = ROLE_FACTORY.get(enum)
    if role_cls is None:
        raise ValueError(f"Unregistered RoleEnum: {enum}")
    return role_cls.__name__
