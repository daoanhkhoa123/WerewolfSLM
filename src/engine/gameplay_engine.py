from src.engine.player_entity_engine import PlayerEntityEngine, GameSetting
from src.engine.vote_engine import VoteBallot, VoteEngine
from src.engine.client_engine.client import ClientRegistry
from src.engine.common.game_context import GameContext, GameTimeEnum

class GameplayEngine:
    def __init__(self, game_setting: GameSetting) -> None:
        self._player_entity_engine = PlayerEntityEngine(game_setting)
        self._vote_engine = VoteEngine()

        self._client_registry = ClientRegistry()
        self._context = GameContext(GameTimeEnum.NIGHT)

    @property
    def player_entity_engine(self) -> PlayerEntityEngine:
        return self._player_entity_engine

    @property
    def vote_engine(self) -> VoteEngine:
        return self._vote_engine

    @property
    def client_registry(self) -> ClientRegistry:
        return self._client_registry
    
    @property
    def context(self) -> GameContext:
        return self._context

    def night_loop(self):
        alives = self.player_entity_engine.get

        for role in self.player_entity_engine.register_roles:
            
            self.vote_engine.clear()
            
            for player in self.player_entity_engine.get_players_by_role(role):
                actionables = player.get_actionables(self.context)
                if actionables is None: # skip
                    continue
                choice = self.client_registry.get(player.name).choose(actionables)
                vote_ballot = VoteBallot(player.name, )
