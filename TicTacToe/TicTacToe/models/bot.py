from TicTacToe.TicTacToe.helper.strategies.botFactory import BotFactory
from players import Player
from playerType import PlayerType

class Bot(Player):
    def __init__(self, player_id, name, symbol, difficulty):
        super().__init__(name, player_id, PlayerType.BOT, symbol)
        self.difficulty = difficulty
        self.bot_strategy = BotFactory.getBot(self.difficulty)

    def decide_cell(self, board):
        return self.bot_strategy.decide_move(board)

