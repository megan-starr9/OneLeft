from core.game.IPlayer import IPlayer
from core.game.Card import Card


class PlayerGameHelper:
    def __init__(self, player: IPlayer):
        self.player = player

    def get_hand(self) -> list[Card]:
        return []

    def get_last_card_played(self) -> Card:
        return ''

    def get_card_pile(self) -> list[Card]:
        return []

    def get_deck_count(self) -> int:
        return 0

    def getOpponentsHandCount(self): list[PlayerHandCount]