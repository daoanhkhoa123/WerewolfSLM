from engine.state_engine.common.role import Role

class Entity:
    ...

class Player(Entity):
    def __init__(self, name:str, role:Role) -> None:
        super().__init__()
        self._name = name
        self.role = role

    @property
    def name(self):
        return self.name