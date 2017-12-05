from core.game.CardType import CardType
from core.game.ColorType import ColorType


class Card:
    def __init__(self, card_type: CardType, color_type: ColorType):
        self.card_type = card_type
        self.color_type = color_type

    @property
    def card_type(self) -> CardType:
        return self.__card_type

    @property
    def color_type(self) -> ColorType:
        return self.__color_type
