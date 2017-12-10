"""
CardAction represents a response that an AI will make when the game engine
asks the AI for an answer. Depending on the action taken, the card property
does not always need to be given.
The class is meant to be a read only class and should be created by the AI
when taking their turn.
"""
from core.game.ActionType import ActionType
from core.game.Card import CardType


class CardAction:
    def __init__(self, action: ActionType, card: CardType = None):
        self._action = action
        self._card = card

    @property
    def action(self) -> ActionType:
        return self._action

    @property
    def card(self) -> CardType:
        return self._card