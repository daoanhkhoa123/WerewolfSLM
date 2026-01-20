from typing import Dict, Optional, Set, Type, final

from src.common.action import BaseAction, LynchAction
from src.common.state import COMMON_STATE_DEFINE, NextStatesT, State


class Role:
    # state - possible states mapping
    state_define: Dict[State, NextStatesT] = COMMON_STATE_DEFINE
    default_state: State = State.SLEEP

    # state - possible actions mapping
    action_define: Dict[State, Set[Type[BaseAction]]] = {State.AWAKE: {LynchAction}}  # unique to each class

    def __init__(self, id) -> None:
        """
        id is to identify the current user, player entity
        """
        self._id = id
        self.state: State = self.default_state

    @property
    def id(self):
        return self._id

    @final
    def get_actionables(self) -> Optional[Set[Type[BaseAction]]]:
        """
        Get all possible actions from the current state
        """
        if self.state not in self.action_define:
            return None
        return self.action_define[self.state]

    @final
    def set_state(self, state: State) -> None:
        """
        Try to transit to new state
        If not valid, then no transition
        """
        next_states = self.state_define[self.state]
        if next_states is None or state not in next_states:
            return
        self.state = state

    ################
    # Macro
    #####################
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
        """
        NOTE: ALWAYS ASSUME THAT action IS POOLED FROM role.get_actionables()
            AND THUS NO NEED TO VALIDATE THAT IT IS VALID

        Execute the action. The result boolean is for checking the validity of the action
            If not valid, then the game manager can call the user to choose again

        The main flow should be
        If valid:
            then action.execute, then return True
        else:
            return False
        """
        raise NotImplementedError(" Must be re-implemented ")

        # all_actionables = self.get_actionables()
        # if all_actionables and type(action) in all_actionables:
        #     action.execute()
        #     return True
        # else:
        #     return False