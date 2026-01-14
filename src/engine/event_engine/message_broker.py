from typing_extensions import Self # type: ignore3
from typing import Optional, Any, Dict, List, NewType

TopicT = NewType("TopicT", str)
MessageKeyT = NewType("MessageKeyT", str)

class Receiver:
    def receive(self, key: MessageKeyT, value: Any) -> bool: ...

class MessageBroker():
    """
    Singleton class 
    topic is to choose the publisher, which has only one as game engine
    key is to defined which payload type to update,
        which i defined in src\engine\client_engine\user_interface.py
    """
    # singleton
    _instance: Optional[Self] = None

    @classmethod
    def init(cls):
        if cls._instance is None:
            cls._instance = cls(safe_init = True)
        return cls._instance

    def __init__(self, *, safe_init:bool=False) -> None:
        if not safe_init: 
            raise RuntimeError("Use MessageBroker.init() to get the singleton instance.")

        self._topics: set[TopicT] = set()
        self._receivers: Dict[TopicT, List[Receiver]] = {}

    @property
    def topics(self) -> set[TopicT]:
        return self._topics

    @property
    def receivers(self) -> Dict[TopicT, List[Receiver]]:
        return self._receivers

    def register_topic(self, topic: TopicT) -> None:
        if topic in self._topics:
            raise ValueError(
                f"Topic '{topic}' is already registered."
            )

        self._topics.add(topic)
        self._receivers[topic] = []

    def register_receiver(self, receiver: Receiver, topic: TopicT) -> None:
        if topic not in self._topics:
            raise KeyError(
                f"Cannot register receiver: topic '{topic}' is not registered."
            )

        self._receivers[topic].append(receiver)

    def notify(self, topic: TopicT, key: MessageKeyT, value: Any, safe_assert:bool = False) -> int:
        if topic not in self._topics:
            raise KeyError(
                f"Cannot publish to topic '{topic}': topic does not exist."
            )

        delivered = 0
        for receiver in self._receivers[topic]:
            if receiver.receive(key, value):
                delivered += 1
    
        if safe_assert and delivered != len(self._receivers[topic]):
            raise RuntimeError(
                f"Message delivery failed for topic '{topic}': "
                f"Delivered {delivered}/{len(self._receivers[topic])} receivers."
            )

        return delivered
