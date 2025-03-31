from models.botDifficulty import BotDifficulty
from models.bot import Bot
from models.symbol import Symbol
from models.playerType import PlayerType
from controllers.gameController import GameController
from models.players import Player

if __name__ == "__main__":
    gc = GameController()

    dimension = 3

    players = [
        Player(name="Ashu", id=1, type=PlayerType.HUMAN, symbol=Symbol('X')),
        Bot(name="Mohit", id=2,  symbol=Symbol('Y'), difficulty=BotDifficulty.EASY)
    ]

    winning_strategies = []

    gc.start_game(dimension, players, winning_strategies)