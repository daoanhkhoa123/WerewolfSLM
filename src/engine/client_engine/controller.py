from typing import Sequence, TypeVar

ChoiceT = TypeVar("ChoiceT")

class Controller:
    def __init__(self, name: int) -> None:
        self._name = name

    @property
    def name(self) -> int:
        return self._name

    def choose(self, choices: Sequence[ChoiceT]) -> ChoiceT: ...