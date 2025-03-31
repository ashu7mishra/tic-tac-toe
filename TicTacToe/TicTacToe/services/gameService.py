from TicTacToe.TicTacToe.models.cellStatus import CellStatus
from TicTacToe.TicTacToe.models.game import Game
from TicTacToe.TicTacToe.models.gameStatus import GameStatus


class GameService:

    def start_game(self, size, players, winning_strategies):
        game = Game.gameBuilder().set_players(players).set_dimension(size).set_winning_strategies(winning_strategies).build()
        return game

    def display_game(self, game):
        game.board.print_board()

    def take_move(self, game):
        current_player = game.players[game.next_turn]
        cell = current_player.decide_cell(game.board)
        cell.player = current_player
        cell.status = CellStatus.FILLED
        game.moves.append(cell)

        if self.check_winner(game, cell):
            game.game_status = GameStatus.COMPLETED
            game.winner = current_player
        elif len(game.moves) == game.board.board_size*game.board.board_size:
            game.game_status = GameStatus.DRAW

        game.next_turn += 1
        game.next_turn %= len(game.players)

    def check_winner(self, game, cell):
        return any(ws.check_winner(game.board, cell) for ws in game.winning_strategies)

    def undo(self, game):
        if not game.moves:
            print("No moves left to undo")
            return

        cell = game.moves.pop()

        for ws in game.winning_strategies:
            ws.undo_handle(game.board, cell)

        cell.status = CellStatus.EMPTY
        cell.player = None

        game.next_turn -= 1
        game.next_turn %= len(game.players)





