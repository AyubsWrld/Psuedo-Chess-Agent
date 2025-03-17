import time
from player import Player
import numpy as np


class Tukvnanawopi:

    class Node:
        def __init__(self, state, player=None, parent=None, depth=0):
            self.state = state
            self.parent = parent
            self.player = player
            self.children = []
            self.moves = 0
            self.captures = 0
            self.evaluation = 0
            self.depth = depth

        def index_to_coordinate(self, row, col):
            col_letter = chr(ord('A') + col - 1)
            row_number = 9 - row
            return f"{col_letter}{row_number + 1}"

        def possible_states(self):
            # generate children of the current state
            if self.player == "W":
                x = np.where(self.state == "W")
                rows = x[0]  # rows where there is a W
                cols = x[1]  # cols where there is a W
                self.check_moves(self.state, rows, cols, self.player)
            if self.player == "B":
                x = np.where(self.state == "B")
                rows = x[0]  # rows where there is a B
                cols = x[1]  # cols where there is a B
                self.check_moves(self.state, rows, cols, self.player)
            return

        def check_moves(self, state, rows, cols, player):
            # check all possible moves for the current player
            # make a move based on the inputed rows and cols
            def make_move(new_state, row, col):
                original_row, original_col = rows[count], cols[count]
                print(f"Making move for {player} from {self.index_to_coordinate(original_row, original_col)} to {self.index_to_coordinate(row, col)}")
                new_state[row, col] = player
                new_state[rows[count], cols[count]] = "O"
                
                print("Possible State:")
                print(new_state)
                return new_state

            # make a capture based on the inputed rows and cols
            def make_capture(new_state, move_row, move_col, capture_row, capture_col):
                original_row, original_col = rows[count], cols[count]
    
                # print the capture move being made
                print(f"Making capture for {player} from {self.index_to_coordinate(original_row, original_col)} to {self.index_to_coordinate(move_row, move_col)}, capturing opponent at {self.index_to_coordinate(capture_row, capture_col)}")
                new_state[capture_row, capture_col] = player
                new_state[move_row, move_col] = "O"
                new_state[rows[count], cols[count]] = "O"
                print("Possible State:")
                print(new_state)
                return new_state

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
                        new_state = make_move(new_state, move_row, move_col)
                        new_node = Tukvnanawopi.Node(new_state, opponent, self, self.depth + 1)
                        self.children.append(new_node)
                        self.moves += 1
                    # if the move tile is already occupied, check if it is the opponent's tile
                    elif self.is_within_bounds(move_row, move_col, state) and state[move_row, move_col] == opponent:
                        # multiply the rows and columns by 2 to get the capture position (to leap over the opponent's piece)
                        capture = (move[0] * 2, move[1] * 2)
                        capture_row, capture_col = rows[count] + capture[0], cols[count] + capture[1]
                        # check if the capture position is within the board and if the space is empty
                        if self.is_within_bounds(capture_row, capture_col, state) and state[capture_row, capture_col] == "O":
                            new_state = make_capture(new_state, move_row, move_col, capture_row, capture_col)
                            new_node = Tukvnanawopi.Node(new_state, opponent, self, self.depth + 1)
                            self.children.append(new_node)
                            self.captures += 1
                count += 1
            return

        def is_within_bounds(self, row, col, state):
            return 0 <= row < state.shape[0] and 0 <= col < state.shape[1]

    def __init__(self, player: Player, time_limit: float, state: np.ndarray):
        self.player = player
        self.time_limit = time_limit
        self.start_time = None
        self.state = state
        self.root = self.Node(state, player)

    def minimax(self, node, depth: int, maximizing_player: bool, alpha: float = -np.inf, beta: float = np.inf):
        '''
        Purpose: The minimax function will explore the state space and find the best possible move for the maximizing
        or minimizing player, as given in the function input.

        Input: the current state of the game given as a numpy 2D array, the current depth of the state given as an integer,
        maximizing player, with max representing a move for the white player and min representing a move for the black
        player, and finally an alpha and beta value (initialized to -inf and inf respectively if no values given)

        Output: As specified by the project description, the output consists of a single move that the agent performs.
        A move is indicated by a pair of squares, where the first indicates which piece is to be moved, and the second
        indicates where the piece is to be moved. For example, in the board configuration above, the horizontal right
        move on row 5 will be represented as C5-E5

        Known Bugs/Problems: At the moment this is completely pseudocode. need various functions implemented by classmates
        before I can proceed. '''
        if depth == 0 or self.is_terminal(node.state, self.player):
            # For leaf nodes, evaluate the state and return the evaluation score and None as the move
            node.evaluation = self.evaluate(node)
            return node.evaluation, None
        
        if not node.children:
            node.possible_states()
        
        best_child = None
        
        if maximizing_player:
            max_eval = float("-inf")
            for child in node.children:
                eval_score, _ = self.minimax(child, depth-1, False, alpha, beta)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_child = child
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_child
        else:
            min_eval = float("inf")
            for child in node.children:
                eval_score, _ = self.minimax(child, depth-1, True, alpha, beta)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_child = child
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_child

    def is_terminal(self, state, player):
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
                (-2, 0), (2, 0), (0, -2), (0, 2),  # Vertical and horizontal jumps
                (-1, -1), (-1, 1), (1, -1), (1, 1),  # Diagonal moves
            ]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if self.root.is_within_bounds(new_row, new_col, state) and state[new_row, new_col] == "O":
                    has_valid_moves = True
                    break

            if has_valid_moves:
                break

        # If current player has no valid moves, the game is also over
        return (white_pieces == 0 or black_pieces == 0 or not has_valid_moves)

    def evaluate(self, node):
        """
        Evaluate the state of the game from the perspective of the current player.
        Returns a value between -1.0 and 1.0.
        """
        if self.is_terminal(node.state, self.player):
            return self.utility(node)
        
        opponent = "W" if self.player == "B" else "B"
    
        player_count = np.count_nonzero(node.state == self.player)
        opponent_count = np.count_nonzero(node.state == opponent)
    
        player_moves = 0
        player_captures = 0
        
        if not node.children:
            mobility_score = 0
        else:
            player_moves = node.moves
            player_captures = node.captures
        
        piece_weight = 1.0
        move_weight = 0.5
        capture_weight = 2.0
    
        piece_advantage = (player_count - opponent_count) / max(1, player_count + opponent_count)
        mobility_advantage = player_moves * move_weight + player_captures * capture_weight
        
        total_score = piece_advantage * piece_weight + mobility_advantage / 20  
        
        return max(min(total_score, 1.0), -1.0)


    def utility(self, node):
        if self.is_terminal(node.state, self.player):
            opponent = "W" if self.player == "B" else "B"
            if np.count_nonzero(node.state == self.player) > 0:
                return 1.0 
            elif np.count_nonzero(node.state == opponent) > 0:
                return -1.0
        return 0.0
    
    def format_move(self, original_state, new_state):
        """
        Compare original and new state to determine the move made.
        Returns a string representation of the move (e.g., "C5-E5").
        """
        # Find where the piece moved from (where original has piece but new has empty)
        moved_from = np.where((original_state != "O") & (new_state == "O"))
        # Find where the piece moved to (where original is empty but new has piece)
        moved_to = np.where((original_state == "O") & (new_state != "O"))
        
        if len(moved_from[0]) > 0 and len(moved_to[0]) > 0:
            from_row, from_col = moved_from[0][0], moved_from[1][0]
            to_row, to_col = moved_to[0][0], moved_to[1][0]
            
            # Convert to board coordinates (e.g., A1, B2)
            from_coord = self.convert_to_coordinate(from_row, from_col)
            to_coord = self.convert_to_coordinate(to_row, to_col)
            
            return f"{from_coord}-{to_coord}"
        
        return "Unknown move"
    
    def convert_to_coordinate(self, row, col):
        """Convert zero-based indices to board coordinates (e.g., A1, B2)"""
        col_letter = chr(ord('A') + col - 1)  # Assuming col starts at 1 in board representation
        row_number = 9 - row  # Assuming row starts at 9 in board representation
        return f"{col_letter}{row_number}"
