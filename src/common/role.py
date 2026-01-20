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
        self._state: State = self.default_state
        self._action_state = self.default_state

    @property
    def id(self):
        return self._id
    
    @property
    def state(self):
        return self._state
    
    @property
    def action_state(self):
        return self._action_state

    @final
    def _set_state(self, state:State) -> bool:        
        """  NOTE: PROGRAMMY FUNCTION, FOR LOCAL USE ONLY """
        next_states = self.state_define[self.state]
        if next_states is None or state not in next_states:
            return False
        
        self._state = state
        return True
    
    @final
    def set_state(self, state: State) -> bool:
        """
        Try to transit to new state
        If not valid, then no transition and return False
        """
        if state == State.SLEEP or state == State.AWAKE or state == State.DEAD:
            raise KeyError("DO not use this function with this")

        return self._set_state(state)
   
    @final
    def get_actionables(self) -> Optional[Set[Type[BaseAction]]]:
        """
        Get all possible actions from the current state
        """
        if self.action_state not in self.action_define:
            return None
        return self.action_define[self.action_state]


    def act(self, action: BaseAction) -> bool:
        """
        NOTE: ALWAYS ASSUME THAT action IS SAMPLED FROM role.get_actionables()
            AND THUS NO NEED TO VALIDATE THAT IT IS VALID

        Execute the action. The result boolean is for checking the validity of the action
            If not valid, then the game manager can call the user to choose again

        The main flow should be
        If valid:
            then action.execute, then return True
        else:
            return False
        """
        action.execute()
        return True

        # all_actionables = self.get_actionables()
        # if all_actionables and type(action) in all_actionables:
        #     action.execute()
        #     return True
        # else:
        #     return False

    @final
    def sleep(self) -> None:
        self._set_state(State.SLEEP)
        self._action_state = self.state

    @final
    def awake(self) -> None:
        self._set_state(State.AWAKE)
        self._action_state = self.state

    @final
    def die(self) -> None:
        self._set_state(State.DEAD)