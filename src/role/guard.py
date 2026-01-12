from typing import List, Optional
from src.engine.state_engine.common.action import ActionEnum
from src.engine.player_entity_manager import GameTimeEnum
from src.engine.state_engine.common.role import Role, RoleTeam
from src.engine.state_engine.common.state import PlayerStateEnum

class GuardRole(Role):
    team = RoleTeam.HUMAN
    
    def get_actionables(self, time: GameTimeEnum) -> Optional[List[ActionEnum]]:
        if time == GameTimeEnum.DAY:
            if self.state != PlayerStateEnum.DEAD:
                return [ActionEnum.NOTHING, ActionEnum.LYNCH]
            
        if time == GameTimeEnum.NIGHT:
            if self.state != PlayerStateEnum.DEAD:
                return [ActionEnum.PROTECT]
            
