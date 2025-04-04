from TicTacToe.TicTacToe.helper.strategies.winningStrategies.winning import Winning


class DiagonalWinningStrategy(Winning):
    def __init__(self):
        self.count1 = {}
        self.count2 = {}

    def check_winner(self, board, cell):
        row = cell.row
        col = cell.col
        symbol = cell.player.symbol

        if row == col:
            if symbol not in self.count1:
                self.count1[symbol] = 0
            self.count1[symbol] += 1

            if self.count1[symbol] == board.board_size:
                return True

        if row + col == board.board_size-1:
            if symbol not in self.count2:
                self.count2[symbol] = 0
            self.count2[symbol] += 1

            if self.count2[symbol] == board.board_size:
                return True

        return False

    def undo_handle(self, board, cell):
        row = cell.row
        col = cell.col
        symbol = cell.player.symbol

        if row == col:
            self.count1[symbol] -= 1

        if row+col == board.board_size-1:
            self.count2 -= 1
