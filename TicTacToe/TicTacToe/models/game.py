from TicTacToe.TicTacToe.helper.gmaeBuilder import GameBuilder
from board import Board
from gameStatus import GameStatus


class Game:
    def __init__(self, dimension, players, winning_strategies):
        self.players = players
        self.winning_strategies = winning_strategies
        self.board = Board(dimension)
        self.moves = []
        self.next_turn = 0
        self.winner = None
        self.game_status = GameStatus.INPROGRESS

    @staticmethod
    def gameBuilder(self):
        return GameBuilder()