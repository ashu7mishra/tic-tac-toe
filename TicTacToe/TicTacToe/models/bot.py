from players import Player
from playerType import PlayerType

class Bot(Player):
    def __init__(self, player_id, name, symbol, difficulty):
        super().__init__(name, player_id, PlayerType.BOT, symbol)
        self.difficulty = difficulty

