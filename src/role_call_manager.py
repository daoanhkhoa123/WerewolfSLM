from src.common.role import Role
from src.common.player_entity import PlayerEntity

class RoleManager:
    def __init__(self, entities:list[PlayerEntity]) -> None:
        self.entities = entities

    def 