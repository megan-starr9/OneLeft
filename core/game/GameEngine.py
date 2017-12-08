from core.game.Card import Card
from core.game.IPlayer import IPlayer
from core.game.GameEngineHelper import GameEngineHelper
from core.game.PlayerGameHelper import PlayerGameHelper
from core.game.GamePlayer import GamePlayer
from typing import List

INITIAL_HAND_SIZE: int = 7
MIN_REQUIRED_PLAYERS: int = 2
MAX_REQUIRED_PLAYERS: int = 10


class GameEngine:
    def __init__(self, players: List[IPlayer], rounds_per_match: int):
        players_count = len(players)
        self._players: List[IPlayer] = players
        if players_count < MIN_REQUIRED_PLAYERS or players_count > MAX_REQUIRED_PLAYERS:
            raise ValueError('Amount of players must be at least 2 and cannot exceed 10')
        self._roundsPerMatch: int = rounds_per_match
        self._deck: List[Card] = GameEngineHelper.create_game_deck()

    def __get_game_players(self, players: List[IPlayer]) -> List[GamePlayer]:
        game_players = []
        for index, player in enumerate(players):
            player_hand = self.__draw_cards(INITIAL_HAND_SIZE)
            game_player = GamePlayer(player, player_hand, index)
            game_players.append(game_player)
        return game_players

    def __draw_cards(self, draw_count: int) -> List[Card]:
        drawn_cards = []
        for n in range(draw_count):
            drawn_cards.append(self._deck.pop(0))
        return drawn_cards

    def __create_player_game_helper(self, active_player: GamePlayer, last_card_played: Card):
        hand = active_player.hand
        last_card_played = last_card_played
        card_pile = []
        deck_count = len(self._deck)
        opp_hand_count = []
        return PlayerGameHelper(hand, last_card_played, card_pile, deck_count, opp_hand_count)

    def start(self):
        current_round: int = 1

        while current_round <= self._roundsPerMatch:
            round_players = self.__get_game_players(self._players)
            round_won = False
            while not round_won:
                print('- Round {0}'.format(current_round))
                active_player: GamePlayer = None
                last_card_played = self.__draw_cards(1)
                for game_player in round_players:
                    active_player = game_player
                    active_player_game_helper = self.__create_player_game_helper(active_player, last_card_played)
                    game_player.player.set_game_helper(active_player_game_helper)
                    game_player.player.take_turn()
                    game_player.hand.pop()
                    if len(game_player.hand) <= 0:
                        round_won = True
                print('{} won the round!'.format(active_player.player.get_player_name()))
                current_round += 1
                self._deck = GameEngineHelper.create_game_deck()
        print('Match is over!')