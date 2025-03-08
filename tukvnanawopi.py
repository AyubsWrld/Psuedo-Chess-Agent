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

    def minimax(state, depth, alpha, beta, maximizing_player):
        if depth == 0 or game over in position # add terminal state verification, later on possibly implement a time constraint
            return evaluation of position

        if maximizing_player: # max moves
            maxEval = "-inf"
            for each child of position: # logan, once we have a "list of children it will be used here"
                eval = self.minimax(child state, depth-1, alpha, beta, false)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha
                    break
            return maxEval
        
        else:
            minEval = "+inf"
            for each child of position:
                eval = self.minimax(child state, depth-1, alpha, beta, true)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return maxEval

    def change_states(self, state: list[list[str]], player: Player) -> list[list[str]]:
        # generate children of the current state

    def is_terminal(self, state: list[list[str]], player: Player) -> bool:
        # is end of game

    def evaluate(self, state: list[list[str]]) -> float:
        # heuristic

    def utility(self, state: list[list[str]]) -> int:
        # -1, 0 or 1
