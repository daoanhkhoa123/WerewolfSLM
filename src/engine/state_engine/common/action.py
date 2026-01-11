from src.engine.state_engine.common.player import PlayerEntity
from enum import auto, IntEnum
from dataclasses import dataclass
from typing import final, Optional

class ActionEnum(IntEnum):
    ############
    #   BASIC ACTION
    ###############
    NOTHING = auto()
    LYNCH = auto()

    ##############
    #   WOLF ACTION
    ##################
    BITE = auto()

    ###################
    #   SEER ACTION
    ########################
    FORETELL = auto()

    ###################
    #   GUARD ACTION
    ########################
    PROTECT = auto()

        ####################
    #   WITCH ACTION
    ###################
    HEAL = auto()
    POISION = auto()

# @dataclass
# class ActionInfo:
#     author: PlayerEntity
#     target: PlayerEntity

# class BaseAction:
#     enum: ActionEnum
#     def __init__(self, author: PlayerEntity, target:Optional[PlayerEntity]) -> None:
#         self._author = author
#         self._target = target

#     @property
#     def author(self) -> PlayerEntity:
#         return self._author
    
#     @property
#     def target(self) -> PlayerEntity:
#         if self._target is None: 
#             raise ValueError(f"Target must be defined for action with target property called for {self.__class__.__name__}")
#         return self._target

# def build(action_enum: ActionEnum, 
#             author: PlayerEntity, target:Optional[PlayerEntity], 
#             *args, **kwargs) -> BaseAction:
#     if action_enum == ActionEnum.NOTHING:
#         return Nothing(author)
    
#     if action_enum == ActionEnum.LYNCH:
#         return Lynch(author, target,  *args, **kwargs)
    
#     if action_enum == ActionEnum.BITE:
#         return Bite(author, target,  *args, **kwargs)
    
#     if action_enum == ActionEnum.FORETELL:
#         return ForeTell(author, target, *args, **kwargs)

#     if action_enum == ActionEnum.HEAL:
#         return Heal(author, target,  *args, **kwargs)
    
#     if action_enum == ActionEnum.POISION:
#         return Poision(author, target,  *args, **kwargs)
    
#     if action_enum == ActionEnum.PROTECT:
#         return Protect(author, target,  *args, **kwargs)
        
#     raise ValueError(f"Unregistered action: {action_enum}")

# ############
# #   BASIC ACTION
# ###############
# class Nothing(BaseAction):
#     enum = ActionEnum.NOTHING

#     def __init__(self, author: PlayerEntity) -> None:
#         super().__init__(author, None)

# class Lynch(BaseAction):
#     enum = ActionEnum.LYNCH

# ##############
# #   WOLF ACTION
# ##################
# class Bite(BaseAction):
#     enum = ActionEnum.BITE

# ###################
# #   SEER ACTION
# ########################
# class ForeTell(BaseAction):
#     enum = ActionEnum.FORETELL

# ###################
# #   GUARD ACTION
# ########################
# class Protect(BaseAction):
#     enum = ActionEnum.PROTECT

# ####################
# #   WITCH ACTION
# ###################
# class Heal(Protect):
#     enum = ActionEnum.HEAL

# class Poision(Bite): 
#     enum = ActionEnum.POISION

# def __validation():
#     # dummy players for construction
#     author = Player("author", None ) # type: ignore
#     target = Player("target", None) # type: ignore

#     # expected enum → class mapping
#     expected = {
#         ActionEnum.NOTHING: Nothing,
#         ActionEnum.LYNCH: Lynch,
#         ActionEnum.BITE: Bite,
#         ActionEnum.FORETELL: ForeTell,
#         ActionEnum.PROTECT: Protect,
#         ActionEnum.HEAL: Heal,
#         ActionEnum.POISION: Poision,
#     }

#     for action_enum, expected_cls in expected.items():
#         try:
#             # NOTHING does not require a target
#             if action_enum == ActionEnum.NOTHING:
#                 action = build(action_enum, author, None)
#             else:
#                 action = build(action_enum, author, target)

#             # check correct class
#             assert isinstance(
#                 action, expected_cls
#             ), f"{action_enum.name} returned {type(action).__name__}, expected {expected_cls.__name__}"

#             # check enum consistency
#             assert (
#                 action.enum == action_enum
#             ), f"{action_enum.name} enum mismatch: {action.enum}"

#             print(f"✔ {action_enum.name} -> {expected_cls.__name__}")

#         except Exception as e:
#             print(f"✘ {action_enum.name} FAILED")
#             raise

#     print("we are good!")

# if __name__ == "__main__":
#     __validation()