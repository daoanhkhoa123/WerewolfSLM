from typing_extensions import Self
from typing import Optional, Dict
from src.engine.client_engine.client import Client
from src.engine.client_engine.controller import Controller
from src.engine.client_engine.user_interface import UserInterface

class ClientRegistry:
    # singleton
    _instance: Optional[Self] = None
    
    @classmethod
    def init(cls) -> Self:
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def __init__(self) -> None:
        self._registry: Dict[str, Client] = {}    
        
    def register(self, client: Client) -> None:
        if client.name in self._registry:
            raise ValueError(
                f"Client '{client.name}' is already registered"
            )
        
        self._registry[client.name] = client

    def get(self, name: str) -> Client:
        if name not in self._registry:
            raise KeyError(f"Client '{name}' is not registered")
        
        return self._registry[name]

class Client:
    def __init__(self, name:str, user_interface: UserInterface, controller: Controller) -> None:
        self._name = name
        self._user_interface = user_interface
        self._controller = controller

    @property
    def name(self):
        return self._name
    
    @property
    def user_interface(self):
        return self._user_interface

    @property
    def controller(self):
        return self._controller
    

    


