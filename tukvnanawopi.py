import time
from player import Player
import numpy as np


class Tukvnanawopi:

    def __init__(self, player: Player, time_limit: float, state: np.ndarray):
        self.player = player
        self.time_limit = time_limit
        self.start_time = None
        self.state = state

    def search_best_move(self):
        # call minimax algorithm in minimax.py file
        # return the best move
        return

    def possible_states(self, state, player: Player):
        # generate children of the current state
        if player == "W":
            x = np.where(state == "W")
            rows = x[0] # rows where there is a W
            cols = x[1] # cols where there is a W
            self.check_moves(state, rows, cols, player)
        if player == "B":
            x = np.where(state == "B")
            rows = x[0] # rows where there is a B
            cols = x[1] # cols where there is a B
            self.check_moves(state, rows, cols, player)
        return

    def check_moves(self, state, rows, cols, player):
        # check if a move is possible, given the state of the board, rows of the player, and columns of the player
        count = 0
        for i in range(len(rows)):
            new_state = state.copy()
            # vertical moves
            if self.is_within_bounds(rows[count] - 2, cols[count], state) and state[rows[count] - 2, cols[count]] == "O":
                new_state[rows[count] - 2, cols[count]] = player
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
            elif self.is_within_bounds(rows[count] + 2, cols[count], state) and state[rows[count] + 2, cols[count]] == "O":
                new_state[rows[count] + 2, cols[count]] = player
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
            # horizontal moves
            elif self.is_within_bounds(rows[count], cols[count] - 2, state) and state[rows[count], cols[count] - 2] == "O":
                new_state[rows[count], cols[count] - 2] = player
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
            elif self.is_within_bounds(rows[count], cols[count] + 2, state) and state[rows[count], cols[count] + 2] == "O":
                new_state[rows[count], cols[count] + 2] = player
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
            # diagonal moves
            elif self.is_within_bounds(rows[count] - 1, cols[count] - 1, state) and state[rows[count] - 1, cols[count] - 1] == "O":
                new_state[rows[count] - 1, cols[count] - 1] = player
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
            elif self.is_within_bounds(rows[count] - 1, cols[count] + 1, state) and state[rows[count] - 1, cols[count] + 1] == "O":
                new_state[rows[count] - 1, cols[count] + 1] = player
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
            elif self.is_within_bounds(rows[count] + 1, cols[count] - 1, state) and state[rows[count] + 1, cols[count] - 1] == "O":
                new_state[rows[count] + 1, cols[count] - 1] = player
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
            elif self.is_within_bounds(rows[count] + 1, cols[count] + 1, state) and state[rows[count] + 1, cols[count] + 1] == "O":
                new_state[rows[count] + 1, cols[count] + 1] = player
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
            count += 1
        return
    
    def is_within_bounds(self, row, col, state):
        return 0 <= row < state.shape[0] and 0 <= col < state.shape[1]

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
        es before I can proceed. '''
        
        '''
        if depth == 0 or game over in position # add terminal state verification, later on possibly implement a time constraint
            return evaluation of position

        if maximizing_player: # max moves
            maxEval = "-inf"
            for each child of position: # logan, once we have a "list of children it will be used here"
                eval = self.minimax(child state, depth-1, alpha, beta, false)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
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
            return maxEval '''

    def is_terminal(self, state, player: Player) -> bool:

        white_pieces = np.count_nonzero(state == "W")
        black_pieces = np.count_nonzero(state == "B")
        
        if white_pieces == 0 or black_pieces == 0:
            return True
        
        has_valid_moves = False
        
        if player == "W":
            positions = np.where(state == "W")
        else:
            positions = np.where(state == "B")
        
        rows = positions[0]
        cols = positions[1]
        
        for i in range(len(rows)):
            row, col = rows[i], cols[i]
            
            directions = [
                (-2, 0), (2, 0), (0, -2), (0, 2),  # Vertical and horizontal jumps ( gotta check validity )
                (-1, -1), (-1, 1), (1, -1), (1, 1),  # Diagonal moves ( gotta check validity ) 
                # Could add jump captures here if needed
            ]
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if self.is_within_bounds(new_row, new_col, state) and state[new_row, new_col] == "O":
                    has_valid_moves = True
                    break
                    
            if has_valid_moves:
                break

        # If current player has no valid moves, the game is also over
        return (white_pieces == 0 or black_pieces == 0 or not has_valid_moves)

    def evaluate(self, state) -> float:
        # heuristic
        return

    def utility(self, state) -> int:
        # -1, 0 or 1
        return
