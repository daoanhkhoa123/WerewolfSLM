from src.engine.common.action import ActionEnum
from src.engine.common.player import PlayerEntity
from src.engine.common.state import PlayerStateEnum
from typing import Iterable

class StateMachine:
    @staticmethod
    def resolve_actions(player_entity: PlayerEntity, actions: Iterable[ActionEnum]) -> PlayerStateEnum:
        # if ActionEnum.LYNCH in actions:
        #     return PlayerStateEnum.DEAD

        # if ActionEnum.PROTECT in actions or ActionEnum.HEAL in actions:
        #     return PlayerStateEnum.ALIVE
        
        # if ActionEnum.BITE in actions or ActionEnum.POISION in actions:
        #     return PlayerStateEnum.DEAD
        
        raise ValueError( f"Unresolved night actions for role {player_entity.name}: {list(actions)}" )