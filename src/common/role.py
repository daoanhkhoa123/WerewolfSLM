from typing import Dict, Optional, Set, Type, final

from src.common.action import BaseAction, LynchAction
from src.common.state import COMMON_STATE_DEFINE, NextStatesT, State


class Role:
    state_define: Dict[State, NextStatesT] = COMMON_STATE_DEFINE
    default_state: State = State.SLEEP
    action_define: Dict[State, Set[Type[BaseAction]]] = {State.AWAKE: {LynchAction}}  # unique to each class

    def __init__(self, id) -> None:
        self._id = id
        self.state: State = self.default_state

    @property
    def id(self):
        return self._id

    @final
    def get_actionables(self) -> Optional[Set[Type[BaseAction]]]:
        if self.state not in self.action_define:
            return None
        return self.action_define[self.state]

    @final
    def set_state(self, state: State) -> None:
        next_states = self.state_define[self.state]
        if next_states is None or state not in next_states:
            return
        self.state = state
    
    @final
    def sleep(self) -> None:
        self.set_state(State.SLEEP)

    @final
    def awake(self) -> None:
        self.set_state(State.AWAKE)

    @final
    def die(self) -> None:
        self.set_state(State.DEAD)

    def act(self, action: BaseAction) -> bool:
        action.execute()
        return True
