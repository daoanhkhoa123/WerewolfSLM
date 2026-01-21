from src.roles.guard import Guard
from src.roles.seer import Seer
from src.roles.villager import Villager
from src.roles.witch import Witch
from src.roles.wolf import Wolf

ROLE_PRIORITY = {Guard: 0,
                 Witch: 1,
                 Wolf:2,
                 Seer:3,
                 Villager:4}