from enum import Enum


class CardType(Enum):
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
    DRAW_TWO = 'draw_two'
    REVERSE = 'reverse'
    SKIP = 'skip'
    WILD_DRAW_FOUR = 'draw_four'
    WILD = 'wild'
