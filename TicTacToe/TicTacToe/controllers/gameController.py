class GameController:
    def __init__(self, gameService):
        self.gameService = gameService

    def start_game(self, size, players, winning_strategies):
        return self.gameService.start_game(size, players, winning_strategies)

    def display_board(self, game):
        self.gameService.display_game(game)

    def take_move(self, game):
        self.gameService.take_move(game)

    def undo_move(self, game):
        self.gameService.undo(game)



"""
    start the game
    display the board
    in loop
        status of the game is in progress
        player makes a move on board
        check the winner
        if no winner or not all cells filled
            change next player index
            other player play

"""