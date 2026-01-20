from src.common.role import Role
from src.common.action import BaseAction
from src.roles.wolf import Wolf
from src.common.state import State

"""
There should be a better way, such as add attribute team 
    to each role to determine if it is a wolf or not
Or add signature to Wolf class, and check that signature?

Also, how to notify the message to the user? Thourgh interface? 
What type of message should be? str? bool?
"""

class ForetellAction(BaseAction):
    def execute(self) -> bool:
        return isinstance(self.target, Wolf)

SEET_ACTION_DEFINE = {
    **Role.action_define,
    State.SLEEP: {ForetellAction}
}

class Seer(Role):
    def __init__(self, id) -> None:
        super().__init__(id)
        self._message = ""

    def act(self, action: BaseAction) -> bool:
        if action.target.state != State.DEAD:
            if action.execute():
                self._message = f"Player {action.target.id} is Wolf"
            else:
                self._message = f"Player {action.target.id} is not Wolf"
            return True
        
        return False
        