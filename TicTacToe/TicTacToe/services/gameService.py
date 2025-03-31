from TicTacToe.TicTacToe.models.cellStatus import CellStatus
from TicTacToe.TicTacToe.models.game import Game


class GameService:

    def start_game(self, size, players, winning_strategies):
        game = Game.gameBuilder().set_players().set_dimension().set_winning_strategies().build()
        return game

    def display_game(self, game):
        game.board.print_board()

    def take_move(self, game):
        current_player = game.players[game.next_turn]
        cell = current_player.decide_cell(game.board)
        cell.player = current_player
        cell.status = CellStatus.FILLED
        game.moves.append(cell)

    def check_winner(self, board, cell):
        



