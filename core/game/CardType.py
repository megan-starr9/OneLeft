"""
CardType is an enum which represents every type of card available in the game.
Descriptions of what each type does are found below.
"""
from enum import Enum


class CardType(Enum):
    """
    ZERO - NINE have no special effects. They are simple numbered cards
    and have no special effect on the game.
    """
    ZERO = 'zero'
    ONE = 'one'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'
    SIX = 'six'
    SEVEN = 'seven'
    EIGHT = 'eight'
    NINE = 'nine'

    """
    DRAW_TWO is an action card that will force the next player to draw two additional cards.
    """
    DRAW_TWO = 'draw_two'

    """
    REVERSE is an action card that will change the order in which players take their turn.
    When playing a 2 player game, the REVERSE acts like a skip.
    """
    REVERSE = 'reverse'

    """
    SKIP is an action card that will skip the next players turn. This means that player
    does not get a chance to play a card.
    """
    SKIP = 'skip'

    """
    WILD_DRAW_FOUR is an action card that will allow you to pick the color of the next
    card played along forcing the next player to draw 4 additional cards.
    """
    WILD_DRAW_FOUR = 'draw_four'

    """
    WILD is an action card that allows you to pick the color of the next card to be played.
    """
    WILD = 'wild'
