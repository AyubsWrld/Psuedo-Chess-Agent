from player import Player
from tukvnanawopi import Tukvnanawopi

class MiniMax:
    '''
    '''
    def __init__(self, player: Player, game: Tukvnanawopi):
        self.player = player
        self.game = game

    def max_value(self, depth: int, alpha: float, beta: float) -> (int, Move):
        # check textbook for reference

    def min_value(self, depth: int, alpha: float, beta: float) -> (int, Move):
        # check textbook for reference


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