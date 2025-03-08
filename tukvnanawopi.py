import time
from player import Player
import minimax
import numpy as np


class Tukvnanawopi:
    def __init__(self, player: Player, time_limit: float, state: np.ndarray):
        self.player = player
        self.time_limit = time_limit
        self.start_time = None
        self.state = state

    def search_best_move(self) -> Move:
        # call minimax algorithm in minimax.py file
        # return the best move
        pass

    def minimax(state: np.ndarray, depth: int,  maximizing_player: bool, alpha: float = -np.inf, beta: float = np.inf) -> int:
        '''
        Purpose: The minimax function will explore the state space and find the best possible move for the maximizing
        or minimizing player, as given in the function input.

        Input: the current state of the game given as a numpy 2D array, the current depth of the state given as an integ
        er, maximizing player, with max representing a move for the white player and min representing a move for the bla
        ck player, and finally an alpha and beta value (initialized to -inf and inf respectively if no values given)

        Output: As specified by the project description, the output consists of a single move that the agent performs.
        A move is indicated by a pair of squares, where the first indicates which piece is to be moved, and the second 
        indicates where the piece is to be moved. For example, in the board configuration above, the horizontal right 
        move on row 5 will be represented as C5-E5

        Known Bugs/Problems: At the moment this is completely pseudocode. need various functions implemented by classmat
        es before I can proceed.
        '''
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
