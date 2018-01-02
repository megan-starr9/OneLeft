##
# Tests for Player.py
#
# All tests in the folder "tests" are executed
# when the "Test" action is invoked.
#
##

from core.game.GameEngineHelper import GameEngineHelper
from core.game.PlayerGameHelper import PlayerGameHelper
from Player import Player
from core.game.IPlayer import IPlayer
from core.game.CardAction import CardAction
from core.game.Card import Card
from core.game.CardType import CardType
from core.game.ActionType import ActionType
from random import shuffle
import unittest

class PlayerTests(unittest.TestCase):

    """
    Ensure name of string type is returned
    """
    def test_name(self):
        player = Player()
        self.assertTrue(type(player.get_player_name()) == str)

    """
    Run through the deck and ensure player actions are valid
        for a random hand
    """
    def test_playsValid(self):
        cards = GameEngineHelper.create_game_deck();
        shuffle(cards)

        hand = []
        for n in range(10):
            hand.append(cards.pop(0))

        player = Player()
        for card in cards:
            print('Testing card - {0} {1}', card.color_type, card.card_type)
            player.set_game_helper(PlayerGameHelper(hand, card, cards, cards.count, 5))
            player_action = player.take_turn()
            if(player_action.action == ActionType.SKIP):
                print('Skipped and drew')
            else:
                print('Card played - {0} {1}', player_action.card.color_type, player_action.card.card_type)
            self.assertTrue(isinstance(player_action, CardAction))
            self.assertTrue(player_action.action == ActionType.SKIP or isValidCard(player_action.card, card))



"""
Helper method to check card validity against another
"""
def isValidCard(card, lastPlayed):
    if not isinstance(card, Card):
        return false
    return card.card_type == lastPlayed.card_type or card.color_type == lastPlayed.color_type or card.card_type == CardType.WILD or card.card_type == CardType.WILD_DRAW_FOUR

"""
Run the suite of tests above
"""
def runPlayerSuite():
    suite = unittest.TestLoader().loadTestsFromTestCase(PlayerTests)
    unittest.TextTestRunner().run(suite)
