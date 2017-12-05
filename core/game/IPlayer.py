

class IPlayer:
    def __init__(self, gameHelper):
        self.gameHelper = gameHelper

    def get_player_name(self):
        """We expect inherting class to implement this"""
        pass

    def takeTurn(self):
        """We expect inherting class to implement this"""
        pass