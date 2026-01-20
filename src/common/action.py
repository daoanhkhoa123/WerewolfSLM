from src.common.role import Role

class BaseAction:
    def __init__(self, target:Role) -> None:
        self._target = target

    @property
    def target(self):
        return self._target

    def execute(self) -> None:  ...

class LynchAction(BaseAction):
    def execute(self) -> None:
        self.target.die()