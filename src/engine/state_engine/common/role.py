from src.engine.state_engine.common.state import PlayerStateEnum
from src.engine.state_engine.common.action import ActionEnum
from src.engine.game_engine import GameTimeEnum
from typing import List, Optional, final, Any
from enum import auto, IntEnum

class RoleTeam(IntEnum):
    HUMAN = auto()
    WOLF = auto()

class Role:
    team: RoleTeam
    def __init__(self, state:PlayerStateEnum) -> None:
        self._state = state
        self._actions:set[ActionEnum] = set()

    @final
    @property
    def state(self) -> PlayerStateEnum:
        return self._state
    
    @final
    @property
    def actions(self) -> set[ActionEnum]:
        return self._actions

    @final
    def take_action(self, action_enum: ActionEnum):
        self._actions.add(action_enum)
    
    def act(self, action: ActionEnum) -> Any:    ...
    def get_actionables(self, time:GameTimeEnum) -> Optional[List[ActionEnum]]:  ...
    

######################## DO NOT USE #################
# @final
# @staticmethod
# def resolve(state:PlayerState, action:BaseAction) -> PlayerState:
#     return StateMachine.resolve(state, action)

## pythonic way would use Type and return class, but this is way too hacky
# def get_actionables(self, time:ActionTime) -> List[Type[BaseAction]]:  return BaseAction