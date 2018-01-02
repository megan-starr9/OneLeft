"""
CardAction represents a response that an AI will make when the game engine
asks the AI for an answer. Depending on the action taken, the card property
does not always need to be given.
The class is meant to be a read only class and should be created by the AI
when taking their turn.
"""

class CardAction:
    def __init__(self, action, card = None, color = None):
        self._action = action
        self._card = card
        self._color = color

    @property
    def action(self):
        return self._action

    @property
    def card(self):
        return self._card

    @property
    def color(self):
        return self._color
