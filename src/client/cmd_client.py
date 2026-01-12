from typing import Any, Sequence, Optional
from src.engine.client_engine.user_interface import UserInterface
from src.engine.client_engine.controller import Controller, ChoiceT
from src.role import get_role_name

class CMDInterface(UserInterface):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def show_game_context(self) -> str:
        return "CURRENT GAME TIME: \n" + f"{self.game_context.time}"
        
    def show_self_context(self) -> str:
        return f"YOU: {self.name} ROLE: {get_role_name(self.self_context.role_enum)}" 

    def show_player_context(self) -> str:
        lines = ["Alive Players:"]
        for name in self.player_context:
            line = name
            if self.player_context[name].is_samewolfteam:
                line = f"{name} (Wolf)"

            lines.append(line)
        
        return "\n".join(lines)
    
    def show_all_context(self) -> str:
        return "\n\n".join([self.show_game_context(), self.show_self_context(), self.show_player_context()])

class CMDController(Controller):
    def __init__(self, name: int, max_trial:int = 2) -> None:
        super().__init__(name)
        self._max_trial = max_trial

    @property
    def max_trial(self) -> int:
        return self._max_trial

    def default_choose(self, choices: Sequence[ChoiceT],
                        zeroth_choice: ChoiceT | None = None) -> ChoiceT:
        if zeroth_choice is not None:
            return zeroth_choice
        return choices[0]

    def choose(self, choices: Sequence[ChoiceT],
        zeroth_choice: Optional[ChoiceT] = None) -> ChoiceT:
        print("Your action:")

        if zeroth_choice is not None:
            print("0:", zeroth_choice)

        for i, choice in enumerate(choices):
            print(f"{i + 1}:", choice)

        trials = 0

        while trials < self.max_trial:
            answer = input("Your Choice: ").strip()
            trials += 1

            if not answer.isdigit():
                print("Invalid input.")
                continue

            idx = int(answer)

            if idx == 0:
                if zeroth_choice is not None:
                    return zeroth_choice
                else:
                    print("Choice 0 not available.")
                    continue

            if 1 <= idx <= len(choices):
                return choices[idx - 1]

            print("Choice out of range.")

        return self.default_choose(choices, zeroth_choice)

        
