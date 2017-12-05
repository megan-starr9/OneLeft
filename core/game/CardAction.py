from core.game.ActionType import *
from core.game.Card import *


class CardAction:
    def __init__(self, action, card):
        self.action = action
        self.card = card

    @property
    def action(self):
        return self.__action

    @property
    def card(self):
        return self.__card