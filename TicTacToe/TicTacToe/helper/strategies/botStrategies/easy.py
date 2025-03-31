from TicTacToe.TicTacToe.helper.strategies.botStrategies.botStrategy import BotStrategy
from TicTacToe.TicTacToe.models.cellStatus import CellStatus


class Easy(BotStrategy):
    def decide_move(self, board):
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell
        return None
