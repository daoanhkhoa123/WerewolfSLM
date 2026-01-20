from src.common.role import Role
from src.common.action import BaseAction
from src.common.state import State, auto2, IntEnum

class WitchState(IntEnum):
    POWER_SLEEP = auto2()

WITCH_DEFINE_STATE = {
    **Role.state_define,
    State.AWAKE: {State.DEAD, WitchState.POWER_SLEEP},
    WitchState.POWER_SLEEP: {State.AWAKE, State.DEAD}
}

class PoisionAction(BaseAction):
    def execute(self) -> None:
        self.target.die()

class HealAction(BaseAction):
    def execute(self) -> None:
        self.target.set_state(State.HEALED)

class Witch(Role):
    action_define  = {WitchState.POWER_SLEEP: {HealAction, PoisionAction}} # type: ignore
    state_define = WITCH_DEFINE_STATE

    def __init__(self, id) -> None:
        super().__init__(id)

        self._can_heal = True
        self._can_poision = True

    def act(self, action: BaseAction) -> bool:
        if isinstance(action, HealAction) and self._can_heal:
            self._can_heal = False
            action.execute()
            return True

        if isinstance(action, PoisionAction) and self._can_poision:
            self._can_poision = False
            action.execute()
            return True

        return False