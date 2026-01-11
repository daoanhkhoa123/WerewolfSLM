from src.engine.state_engine.common.action import ActionEnum
from src.engine.state_engine.common.role import Role
from src.engine.state_engine.common.state import PlayerStateEnum
from typing import Iterable

class StateMachine:
    @staticmethod
    def resolve_actions(role:Role, actions: Iterable[ActionEnum]) -> PlayerStateEnum:
        if ActionEnum.LYNCH in actions:
            return PlayerStateEnum.DEAD

        if ActionEnum.PROTECT in actions or ActionEnum.HEAL in actions:
            return PlayerStateEnum.ALIVE
        
        if ActionEnum.BITE in actions or ActionEnum.POISION in actions:
            return PlayerStateEnum.DEAD
        
        raise ValueError( f"Unresolved night actions for role {role}: {list(actions)}" )