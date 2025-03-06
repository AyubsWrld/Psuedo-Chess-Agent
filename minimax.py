from player import Player
from tukvnanawopi import Tukvnanawopi

class MiniMax:
    def __init__(self, player: Player, game: Tukvnanawopi):
        self.player = player
        self.game = game

    def max_value(self, depth: int, alpha: float, beta: float) -> (int, Move):
        # check textbook for reference

    def min_value(self, depth: int, alpha: float, beta: float) -> (int, Move):
        # check textbook for reference
