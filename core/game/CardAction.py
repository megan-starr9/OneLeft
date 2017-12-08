from core.game.ActionType import *
from core.game.Card import *


class CardAction:
    def __init__(self, action, card):
        self._action = action
        self._card = card

    @property
    def action(self):
        return self._action

    @property
    def card(self):
        return self._card