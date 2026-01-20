from src.common.role import Role
from src.common.action import BaseAction
from src.common.state import State


class ProtectAction(BaseAction):
    def execute(self) -> None:
        self.target.set_state(State.PROTECTED)

GUARD_ACTION_DEFINE = {
    **Role.action_define,
    State.SLEEP: {ProtectAction}
}

class Guard(Role):
    action_define = GUARD_ACTION_DEFINE

    def __init__(self, id) -> None:
        super().__init__(id)
        self._last_protected_id = None

    def act(self, action: BaseAction) -> bool:
        if isinstance(action, ProtectAction) and action.target.id != self._last_protected_id:
            self._last_protected_id = action.target.id
            action.execute()
            return True
        
        return False

