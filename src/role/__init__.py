from enum import IntEnum, auto
from src.engine.state_engine.common.role import Role, RoleTeam
from src.role.guard import GuardRole
from src.role.seer import SeerRole
from src.role.villager import VillagerRole
from src.role.wolf import WolfRole

__all__ = ["RoleEnum", "build_role"]

class RoleEnum(IntEnum):
    VILLAGER = auto()
    WOLF = auto()
    GUARD = auto()
    SEER = auto()

def build_role(enum: RoleEnum, *args, **kwargs) -> Role:
    if enum is RoleEnum.VILLAGER:
        return VillagerRole(*args, **kwargs)

    if enum is RoleEnum.WOLF:
        return WolfRole(*args, **kwargs)

    if enum is RoleEnum.GUARD:
        return GuardRole(*args, **kwargs)

    if enum is RoleEnum.SEER:
        return SeerRole(*args, **kwargs)

    raise ValueError(f"Unregistered RoleEnum: {enum}")