class PlayerHandCount:
    def __init__(self, player_name: str, hand_count: int):
        self.player_name = player_name
        self.hand_count = hand_count

    @property
    def player_name(self) -> str:
        return self.__player_name

    @property
    def hand_count(self) -> int:
        return self.___hand_count
