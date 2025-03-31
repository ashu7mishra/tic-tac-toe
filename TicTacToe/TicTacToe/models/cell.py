from cellStatus import CellStatus


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.player = None
        self.status = CellStatus.EMPTY

    def display(self):
        if self.status == CellStatus.EMPTY:
            print("| - |", end="")
        else:
            print(f"| {self.player.Symbol.symbol} |", end="")
