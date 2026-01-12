from typing import TYPE_CHECKING, final, Any, Optional, List
from src.engine.state_engine.common.state import PlayerStateEnum
from src.engine.state_engine.common.action import ActionEnum
from src.engine.player_entity_manager import GameTimeEnum

if TYPE_CHECKING:
    from src.engine.state_engine.common.role import Role

class PlayerEntity:
    def __init__(self, name: str) -> None:
        self._name = name         
        self._role = None
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def role(self) -> "Role":
        if self._role is None:
            raise ValueError(f"Player '{self._name}' has no role assigned. Use {self.build_role.__name__}() first.")
        
        return self._role
    
    def build_role(self, role:Role) -> None:
        self._role = role

    ###################################
    #   STRAIGHT OUT COPIED FROM ROLE
    ######################################
    @final
    @property
    def state(self) -> PlayerStateEnum:
        return self.role._state
    
    @final
    @property
    def actions(self) -> set[ActionEnum]:
        return self.role._actions

    @final
    def take_action(self, action_enum: ActionEnum):
        self.role._actions.add(action_enum)
    
    def act(self, action: ActionEnum) -> Any:
        return self.role.act(action)
    
    def get_actionables(self, time:GameTimeEnum) -> Optional[List[ActionEnum]]:
        return self.role.get_actionables(time)
    