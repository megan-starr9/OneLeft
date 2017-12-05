from core.game.CardAction import CardAction


class IPlayer:
    def __init__(self, game_helper):
        self.game_helper = game_helper

    def get_player_name(self) -> str:
        pass

    def take_turn(self) -> CardAction:
        pass
