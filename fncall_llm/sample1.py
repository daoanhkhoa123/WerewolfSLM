class Role:
    ...

class Player:
    def __init__(self, role:Role) -> None:
        self.defended = False
        self.role = role
        self.alive = False

    def get_defened(self):
        self.defended = True

    def get_undefended(self):
        self.defended = False

    def die(self):
        if self.defended:
            return
        self.alive = False

class Witch(Role):
    def __init__(self) -> None:
        super().__init__()
        self.can_defend = True
        self.can_attack = False

    def defend(self, player:Player):
        player.get_defened()

    def kill(self, player: Player):
        player.die()


class GameEngine: