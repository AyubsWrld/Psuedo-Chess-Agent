import time
from player import Player
import minimax


class Tukvnanawopi:
    def __init__(self, player: Player, time_limit: float, state: list[list[str]]):
        self.player = player
        self.time_limit = time_limit
        self.start_time = None
        self.state = state

    def search_best_move(self) -> Move:
        # call minimax algorithm in minimax.py file
        # return the best move

    def possible_states(self, state: list[list[str]], player: Player) -> list[list[str]]:
        # generate children of the current state

    def is_terminal(self, state: list[list[str]], player: Player) -> bool:
        # is end of game

    def evaluate(self, state: list[list[str]]) -> float:
        # heuristic

    def utility(self, state: list[list[str]]) -> int:
        # -1, 0 or 1
