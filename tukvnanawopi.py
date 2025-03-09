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
        # check all possible moves for the current player
        # make a move based on the inputed rows and cols
        def make_move(new_state, row, col):
            new_state[row, col] = player
            new_state[rows[count],cols[count]] = "O"
            print("Possible State:")
            print(new_state)
        # make a capture based on the inputed rows and cols
        def make_capture(new_state, move_row, move_col, capture_row, capture_col):
            new_state[capture_row, capture_col] = player
            new_state[move_row, move_col] = "O"
            new_state[rows[count],cols[count]] = "O"
            print("Possible State:")
            print(new_state)
        # get the opposite of the current player
        def get_opponent():
            if player == "W":
                opponent = "B"
            else:
                opponent = "W"
            return opponent
        
        count = 0
        moves = [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        opponent = get_opponent()
        for i in range(len(rows)):
            new_state = state.copy()
            for move in moves:
                # keep track of the col and row for the move
                move_row, move_col = rows[count] + move[0], cols[count] + move[1]
                # check if the move is within the board and if the space is empty
                if self.is_within_bounds(move_row, move_col, state) and state[move_row, move_col] == "O":
                    make_move(new_state, move_row, move_col)
                # if the move tile is already occupied, check if it is the opponent's tile
                elif self.is_within_bounds(move_row, move_col, state) and state[move_row, move_col] == opponent:
                    # multiply the rows and columns by 2 to get the capture position (to leap over the opponent's piece)
                    capture = (move[0]*2, move[1]*2)
                    capture_row, capture_col = rows[count] + capture[0], cols[count] + capture[1]
                    # check if the capture position is within the board and if the space is empty
                    if self.is_within_bounds(capture_row, capture_col, state) and state[capture_row, capture_col] == "O":
                        make_capture(new_state, move_row, move_col, capture_row, capture_col)
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
