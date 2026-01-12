from enum import auto, IntEnum

class PlayerStateEnum(IntEnum):
    ##############
    #   BASIC STATE
    ##################
    DEAD = auto()
    ALIVE = auto()
    SLEEP = auto()

    #################
    #   WOLF STATE
    ################

    #################
    #   SEER STATE
    ################
    
    ###################
    #   GUARD STATE
    ########################

    ######################
    #   HUNTER STATE
    #########################
    REVENGENCE = auto()

    ###################
    #   WITCH STATE 
    ##################
    FIRST_NIGHT_SLEEP = auto()
