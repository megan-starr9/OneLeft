from core.game.CardAction import CardAction
from core.game.PlayerGameHelper import PlayerGameHelper


class IPlayer:
    def __init__(self):
        self._game_helper: PlayerGameHelper = None

    def get_player_name(self) -> str:
        pass

    def take_turn(self) -> CardAction:
        pass

    def set_game_helper(self, game_helper: PlayerGameHelper):
        self._game_helper = game_helper

    def get_game_helper(self) -> PlayerGameHelper:
        return self._game_helper
