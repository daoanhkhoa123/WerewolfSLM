from typing import List, Optional
from engine.state_engine.common.action import ActionEnum, ActionTime
from engine.state_engine.common.role import Role, RoleTeam
from engine.state_engine.common.state import PlayerStateEnum

class WolfRole(Role):
    team = RoleTeam.WOLF

    def get_actionables(self, time: ActionTime) -> Optional[List[ActionEnum]]:
        if time == ActionTime.DAY:
            if self.state != PlayerStateEnum.DEAD:
                return [ActionEnum.NOTHING, ActionEnum.LYNCH]
            
        if time == ActionTime.NIGHT:
            if self.state != PlayerStateEnum.DEAD:
                return [ActionEnum.NOTHING, ActionEnum.BITE]
        
    

