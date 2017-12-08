from core.game.CardType import CardType
from core.game.ColorType import ColorType


class Card:
    def __init__(self, card_type: CardType, color_type: ColorType):
        self._card_type: CardType = card_type
        self._color_type: ColorType = color_type

    @property
    def card_type(self) -> CardType:
        return self._card_type

    @property
    def color_type(self) -> ColorType:
        return self._color_type
