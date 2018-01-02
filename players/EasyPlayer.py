# File For Easy Player
from core.game.IPlayer import IPlayer
from core.game.CardAction import CardAction
from core.game.ActionType import ActionType


class Player(IPlayer):
    """
    Player's class implemented version of get_player_name.
    Change the name returned in this method to name your AI.
    """
    def get_player_name(self):
        return 'Easy AI'

    """
    Player's class implemented version of take_turn.
    This the CardAction returned here is used by the game engine to
    play your AIs card against your opponents. Modify this method
    as much as necessary to create the logic for your AI.
    """
    def take_turn(self):
        card = self.get_game_helper().get_hand()[0]
        return CardAction(ActionType.PLAY, card)
