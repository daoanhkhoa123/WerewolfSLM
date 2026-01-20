from src.common.role import Role

class PlayerEntity:
    def __init__(self, name:str, role:Role) -> None:
        self.name = name
        self.role = role

    @property
    def state(self):
        return self.role.state
    
    