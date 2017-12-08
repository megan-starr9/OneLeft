from core.game.IPlayer import IPlayer
from core.game.CardAction import CardAction
from core.game.ActionType import ActionType


class Player(IPlayer):
    def get_player_name(self) -> str:
        return 'My Cool Name'

    def take_turn(self) -> CardAction:
        card = self.get_game_helper().get_hand()[0]
        return CardAction(ActionType.PLAY, card)
