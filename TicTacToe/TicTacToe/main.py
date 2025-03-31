from TicTacToe.TicTacToe.helper.strategies.winningStrategies.diagonalWS import DiagonalWinningStrategy
from TicTacToe.TicTacToe.models.gameStatus import GameStatus
from TicTacToe.TicTacToe.services.gameService import GameService
from models.botDifficulty import BotDifficulty
from models.bot import Bot
from models.symbol import Symbol
from models.playerType import PlayerType
from controllers.gameController import GameController
from models.players import Player

if __name__ == "__main__":
    gs = GameService()
    gc = GameController(gs)

    dimension = 3

    players = [
        Player(name="Ashu", id=1, type=PlayerType.HUMAN, symbol=Symbol('X')),
        Bot(name="Mohit", id=2,  symbol=Symbol('Y'), difficulty=BotDifficulty.EASY)
    ]

    winning_strategies = [DiagonalWinningStrategy()]

    game = gc.start_game(dimension, players, winning_strategies)

    # display board
    gc.display_board(game)

    # until game in progress take input

    while game.game_status == GameStatus.INPROGRESS:
        gc.take_move(game)
        gc.display_board(game)
        undo_answer = input("If you want to undo your last move, press 1: ")
        if undo_answer == "1":
            print("undo....")
            gc.undo_move(game)
            gc.display_board(game)

    if game.game_status == GameStatus.COMPLETED:
        print(f"winner: {game.winner}")
    elif game.game_status == GameStatus.DRAW:
        print("draw")