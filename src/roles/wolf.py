from src.common.role import Role
from src.common.action import BaseAction
from src.common.state import State
from typing import Dict, Set, Type

class BiteAction(BaseAction):
    def execute(self) -> None:
        self.target.die()

WOLF_ACTION_DEFINE = {
    **Role.action_define,
    State.SLEEP: {BiteAction}
}

class Wolf(Role):
    action_define: Dict[State, Set[Type[BaseAction]]]  = WOLF_ACTION_DEFINE
