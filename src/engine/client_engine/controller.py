from typing import Sequence, TypeVar, Optional

ChoiceT = TypeVar("ChoiceT")

class Controller:
    def __init__(self, name: int) -> None:
        self._name = name

    @property
    def name(self) -> int:
        return self._name

    def default_choose(self, choices: Sequence[ChoiceT], 
                       zeroth_choice: Optional[ChoiceT] = None) -> ChoiceT: ...        

    def choose(self, choices: Sequence[ChoiceT], 
               zeroth_choice: Optional[ChoiceT] = None) -> ChoiceT:
        return self.default_choose(choices, zeroth_choice)