"""
ActionType is an enum descriptions the several types of actions an AI can take
during their turn.
"""
from enum import Enum


class ActionType(Enum):
    """
    Use SKIP when you have no legal cards to play on your turn. In addition,
    You can also use skip to strategically not spend any of your cards. Either
    scenario will result in your AI adding an addition card to their hand
    from the deck.
    """
    SKIP = 'skip'

    """
    Use PLAY when you have a legal card to play. 
    """
    PLAY = 'play'
