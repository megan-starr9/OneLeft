
class IPlayer:
    """
    IPlayer is the base abstract that the the GameEngine will use to play AIs
    against one another. The game engine expects to be able to call any of
    the public methods below.

    When extending from IPlayer, implement the follow methods,
    descriptions for what each does can be found below:
      get_player_name()
      take_turn()
    """
    def __init__(self):
        self._game_helper = None

    """
    The extending class is expected to implement def get_player_name.
    Method should return a string to display as the AIs name for logging.
    """
    def get_player_name(self):
        pass

    """
    The extending class is expected to implement take_turn.
    This method is called by the game engine to decide what card the AI
    will play for its turn.
    """
    def take_turn(self):
        pass

    """
    set_game_helper is already implemented and should not be modified.
    This method will be called by the game engine before calling the
    take_turn method. This gives the extending class a reference to
    a PlayerGameHelper to use for deciding what card to play during
    the take_turn method.
    """
    def set_game_helper(self, game_helper):
        self._game_helper = game_helper

    """
    get_game_helper is already implemented and should not be modified.
    This is a helper method to be used during the take_turn method as it
    provides access into some of the game's current state.
    """
    def get_game_helper(self):
        return self._game_helper
