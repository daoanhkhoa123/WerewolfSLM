from enum import IntEnum
from typing import Dict, Optional, Set

class auto2:
    """ 
    This class is for continious enum define, 
    so that the mapping does not overide the old one

    ```python
    from enum import IntEnum

    # --- Example subclasses ---
    class Color(IntEnum):
        RED = auto2()

    class Shape(IntEnum):
        CIRCLE = auto2()

    class Animal(IntEnum):
        DOG = auto2()

    Color.RED -> 0
    Shape.CIRCLE -> 1
    Animal.DOG -> 2
    ```
    """
    _global_count = -1
    def __new__(cls) -> int:
        cls._global_count += 1
        return cls._global_count

class State(IntEnum):
    """ 
    Common state that is every role can have in
    """
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

"""
Mapping state to possible states that everyclass can do this

So state define of a role should be common + unique map
"""
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
