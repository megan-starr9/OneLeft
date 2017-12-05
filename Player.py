from core.game.IPlayer import IPlayer
from core.game.CardAction import CardAction


class Player(IPlayer):
    def get_player_name(self) -> str:
        return 'My Cool Name'

    def take_turn(self) -> CardAction:
        return ''
