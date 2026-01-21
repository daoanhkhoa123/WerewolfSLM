from typing import Any
from src.client import Client, ClientArg
from src.roles import ROLE_PRIORITY

class _Vote:
    def __init__(self) -> None:
        self._ballot = dict()

    def vote(self, obj):
        self._ballot[obj] = self._ballot.get(obj, 0) + 1

    def get_winner(self):
        return max(self._ballot.keys(), key=lambda x: self._ballot[x])
    
    def reset(self):
        self._ballot = dict()

class RoleCallManager:
    def __init__(self, clients:list[Client], everyone: bool=False) -> None:
        _current_role = None
        for c in clients:
            if _current_role is None:
                _current_role = c.entity.role
            if not everyone and _current_role != c.entity.role:
                raise ValueError("Must be same role")
        self._role = _current_role
        self._clients = clients
        self._vote = _Vote()

    @property
    def role(self):
        return self._role

    @property
    def clients(self):
        return self._clients
    
    @property
    def vote_engine(self):
        return self._vote

    def __call__(self) -> Any:
        self.vote_engine.reset()
        for client in self.clients:
            self.vote_engine.vote(client.decide())

        for client in self.clients:
            client.entity.role.act(self.vote_engine.get_winner())

class RoleCallManagerFactory:
    def __call__(self, clients:list[Client]) -> dict[Any, RoleCallManager]:
        role_client = {-1: clients}
        for c in clients:
            if c.entity.role not in role_client:
                role_client[c.entity.role] = [c] # type: ignore
            else:
                role_client[c.entity.role].append(c) # type: ignore

        role_rcm = {k:RoleCallManager(role_client[k]) for k in role_client}
        return role_rcm
    
class GameEngine:
    def __init__(self, clients:list[Client]) -> None:
        self.rcm = RoleCallManagerFactory()(clients)
        self.clients = clients

    def day_call(self):
        for c in self.clients:
            c.entity.role.awake()

        self.rcm[-1]()  # everyone vote

    def night_call(self):
        for c in self.clients:
            c.entity.role.sleep()

        for role in self.rcm:
            self.rcm[role]()
    

    