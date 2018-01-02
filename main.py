from core.game.GameEngine import GameEngine
from Player import Player
# from players.EasyPlayer import Player as EasyPlayer
# from players.HardPlayer import Player as HardPlayer
# from players.MediumPlayer import Player as MediumPlayer
from players.RandomPlayer import RandomPlayer

from tests.PlayerTests import runPlayerSuite

def main():
    players = [Player(), RandomPlayer()]

    game_engine = GameEngine(players, 10)
    game_engine.start()

def main_test():
    runPlayerSuite()

"""
Run the main game program
"""
main()

"""
Run the program Tests
"""
#main_test()
