from abc import ABC, abstractmethod


class Winning(ABC):

    @abstractmethod
    def check_winner(self, board, cell):
        pass

    @abstractmethod
    def undo_handle(self, board, cell):
        pass
