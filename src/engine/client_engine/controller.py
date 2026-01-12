from typing import Sequence, TypeVar, Optional, Tuple

ChoiceKeyT = TypeVar("ChoiceKeyT")
ChoiceValueT = TypeVar("ChoiceValueT")

class Controller:
    def __init__(self, name: int) -> None:
        self._name = name

    @property
    def name(self) -> int:
        return self._name

    def default_choose(self, choices: Sequence[ChoiceKeyT], 
                       zeroth_choice: Optional[ChoiceValueT] = None) -> Tuple[ChoiceKeyT, ChoiceValueT]: ...        

    def choose(self, choices: Sequence[ChoiceKeyT], 
                       zeroth_choice: Optional[ChoiceValueT] = None) -> Tuple[ChoiceKeyT, ChoiceValueT]: ...        
