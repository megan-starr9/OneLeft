# File For Easy Player
from core.game.IPlayer import IPlayer
from core.game.CardAction import CardAction


class Player(IPlayer):
    def get_player_name(self) -> str:
        return 'Easy Player'

    def take_turn(self) -> CardAction:
        return ''
