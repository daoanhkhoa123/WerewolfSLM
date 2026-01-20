from enum import IntEnum
from typing import Dict, Optional, Set

class auto2:
    _global_count = -1
    def __new__(cls) -> int:
        cls._global_count += 1
        return cls._global_count

"""
Q: Why Healed is a state but not bited?
A: Try it is
"""
class State(IntEnum):
    AWAKE = auto2()
    SLEEP = auto2()
    DEAD = auto2()

    ####################
    #   WOLF
    ####################
    BITED = auto2()

    ##################
    #   WITCH
    ################
    HEALED = auto2()
    POSIONED = BITED

    ################
    #   GUARD
    ###############
    PROTECTED = HEALED


NextStatesT = Optional[Set[State]]

COMMON_STATE_DEFINE: Dict[State, NextStatesT] = {
    State.AWAKE: {State.SLEEP, State.DEAD},
    State.SLEEP: {State.AWAKE},
    State.DEAD: None,

    ####################
    #   WOLF
    ####################
    State.BITED: {State.DEAD},

    ##################
    #   WITCH
    ################
    State.HEALED: {State.AWAKE}
    # posion is the same

    ################
    #   GUARD
    ###############
    # protected is the same
}
