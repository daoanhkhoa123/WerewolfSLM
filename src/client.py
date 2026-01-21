from src.common.player_entity import PlayerEntity
from src.common.action import BaseAction
from dataclasses import dataclass

class Interface:
    ...

class Controller:
    def __init__(self, entity: PlayerEntity) -> None:
        self.entity = entity

    def decice(self) -> BaseAction:
        ...

@dataclass
class ClientArg:
    id: str
    interface:Interface
    ontroller:Controller
    entity:PlayerEntity


class Client:
    def __init__(self, id, interface:Interface, controller:Controller, entity:PlayerEntity) -> None:
        self.interface = interface
        self.controller = controller

    @property
    def entity(self):
        return self.controller.entity

    def decide(self):
        return self.controller.decice()