"""
The Card represents a card object from the game. Every card contains a color
along with a type. Refer to CardType and ColorType for full descriptions
of each. This class is meant to be a read-only class, meaning once the object
is created, it cannot be modified.
"""

class Card:
    def __init__(self, card_type, color_type):
        self._card_type = card_type
        self._color_type = color_type

    @property
    def card_type(self):
        return self._card_type

    @property
    def color_type(self):
        return self._color_type

    def get_card_text(self):
        return '{} {}'.format(self._color_type, self.color_type)
