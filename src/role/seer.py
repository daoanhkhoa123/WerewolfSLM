from typing import Any, List, Optional
from engine.state_engine.common.action import ActionEnum, ActionTime, BaseAction
from engine.state_engine.common.role import Role, RoleTeam
from engine.state_engine.common.state import PlayerStateEnum

class SeerRole(Role):
    team = RoleTeam.HUMAN

    def get_actionables(self, time: ActionTime) -> Optional[List[ActionEnum]]:
        if time == ActionTime.DAY:
            if self.state != PlayerStateEnum.DEAD:
                return [ActionEnum.NOTHING, ActionEnum.LYNCH]
            
        if time == ActionTime.NIGHT:
            if self.state != PlayerStateEnum.DEAD:
                return [ActionEnum.FORETELL]
        
    
    def act(self, action: BaseAction) -> Any:
        if action.enum == ActionEnum.FORETELL:
            if action.target._role.team == RoleTeam.WOLF:
                return True
            else:
                return False
            

    