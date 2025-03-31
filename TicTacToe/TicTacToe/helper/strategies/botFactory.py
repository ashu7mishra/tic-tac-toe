#add abstract class yourself
from TicTacToe.TicTacToe.helper.strategies.botStrategies.easy import Easy
from TicTacToe.TicTacToe.models.botDifficulty import BotDifficulty


class BotFactory:

    @staticmethod
    def getBot(difficulty):
        if difficulty == BotDifficulty.EASY:
            return Easy()
