import time
from player import Player
import numpy as np
import math


class Tukvnanawopi:

    class Node:
        def __init__(self, state, player=None, parent=None, depth=0, move=None):
            self.state = state
            self.parent = parent
            self.player = player
            self.children = []
            self.moves = 0
            self.captures = 0
            self.evaluation = 0
            self.depth = depth
            self.move = move

        def index_to_coordinate(self, row, col):
            row_number = 9 - row
            col_list = "ABCDEFGHI"
            col_letter = col_list[col]
            return f"{col_letter}{row_number}"

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
                """
                Purpose: Makes a move for the current player by updating the game state
                
                Input:
                    - new_state (2D array): A matrix representing the current state of the game board.
                    - row (int): The row index of the new position where the player is making a move.
                    - col (int): The column index of the new position where the player is making a move.
                
                Output:
                    - new_state (2D array): The updated game state after the move is made.
                    - move_tuple (tuple): A tuple representing the move made, containing the original and new coordinates of the piece.
                """
                # made a modification here so that make_move will return the move that resulted in the new state
                original_row, original_col = rows[count], cols[count]
                original_coord = self.index_to_coordinate(original_row, original_col)
                new_coord = self.index_to_coordinate(row, col)
                print(f"Making move for {player} from {original_coord} to {new_coord}")
                move_tuple = (original_coord, new_coord) # tuple representing which piece was moved
                new_state[row, col] = player
                new_state[rows[count], cols[count]] = "O"
                
                print("Possible State:")
                print(new_state)
                return new_state, move_tuple


            # make a capture based on the inputed rows and cols
            def make_capture(new_state, move_row, move_col, capture_row, capture_col):
                """
                Purpose: Makes a capture move for the current player by updating the game state and capturing the opponent's piece.
                
                Input:
                    - new_state (2D array): A matrix representing the current state of the game board.
                    - move_row (int): The row index of the new position where the player is moving the piece.
                    - move_col (int): The column index of the new position where the player is moving the piece.
                    - capture_row (int): The row index of the opponent's piece being captured.
                    - capture_col (int): The column index of the opponent's piece being captured.
                
                Output:
                    - new_state (2D array): The updated game state after the capture move is made.
                    - move_tuple (tuple): A tuple representing the move made, containing the original, new, and captured coordinates of the piece.
                """
                original_row, original_col = rows[count], cols[count]
                original_coord = self.index_to_coordinate(original_row, original_col)
                move_coord = self.index_to_coordinate(move_row, move_col)
                capture_coord = self.index_to_coordinate(capture_row, capture_col)
                
                print(f"Making capture for {player} from {original_coord} to {move_coord}, capturing opponent at {capture_coord}")
                
                new_state[capture_row, capture_col] = player
                new_state[move_row, move_col] = "O"
                new_state[rows[count], cols[count]] = "O"
                
                print("Possible State:")
                print(new_state)
                
                move_tuple = (original_coord, move_coord, capture_coord)
                return new_state, move_tuple

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
                        new_state, move_tuple = make_move(new_state, move_row, move_col)
                        new_node = Tukvnanawopi.Node(new_state, opponent, self, self.depth + 1, move_tuple)
                        self.children.append(new_node)
                        self.moves += 1
                    # if the move tile is already occupied, check if it is the opponent's tile
                    elif self.is_within_bounds(move_row, move_col, state) and state[move_row, move_col] == opponent:
                        # multiply the rows and columns by 2 to get the capture position (to leap over the opponent's piece)
                        capture = (move[0] * 2, move[1] * 2)
                        capture_row, capture_col = rows[count] + capture[0], cols[count] + capture[1]
                        # check if the capture position is within the board and if the space is empty
                        if self.is_within_bounds(capture_row, capture_col, state) and state[capture_row, capture_col] == "O":
                            new_state, move_tuple = make_capture(new_state, move_row, move_col, capture_row, capture_col)
                            new_node = Tukvnanawopi.Node(new_state, opponent, self, self.depth + 1, move_tuple)
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

    def minimax(self, node: Node, depth:int, maximizing_player: bool, alpha: float = -np.inf, beta: float = np.inf) -> int:
        '''
        Purpose: The minimax function will explore the state space and find the best possible move for the maximizing
        or minimizing player, as given in the function input.

        Input: the current state of the game given as a numpy 2D array, the current depth of the state given as an integer,
        maximizing player, with max representing a move for the white player and min representing a move for the black
        player, and finally an alpha and beta value (initialized to -inf and inf respectively if no values given)

        Output: As specified by the project description, the output consists of a single move that the agent performs.
        A move is indicated by a pair of squares, where the first indicates which piece is to be moved, and the second
        indicates where the piece is to be moved. For example, in the board configuration above, the horizontal right
        move on row 5 will be represented as C5-E5'
        '''

        if self.is_terminal(node.state, self.player):
            return self.evaluate(node), node.move
        
        if maximizing_player:
            print("here")
            max_eval = -math.inf
            best_move = None
            node.possible_states() # generate the children of the 
            for child in node.children:
                eval, _ = self.minimax(child, False, alpha, beta) # call minimax for minimizing player
                if eval > max_eval:
                    max_eval = eval
                    best_move = child.move
                alpha = max(alpha, eval)
                if beta <= alpha: #prune
                    break
            return max_eval, best_move
        else:
            print("here")
            min_eval = math.inf
            best_move = None
            node.possible_states() # generate the children of the 
            for child in node.children:
                eval, _ = self.minimax(child, True, alpha, beta) # call minimax for minimizing player
                if eval < min_eval:
                    min_eval = eval
                    best_move = child.move
                beta = min(alpha, eval)
                if beta <= alpha: #prune
                    break
            return min_eval, best_move

        

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
                if self.root.is_within_bounds(new_row, new_col, state) and state[new_row, new_col] == "O":
                    has_valid_moves = True
                    break

            if has_valid_moves:
                break

        # If current player has no valid moves, the game is also over
        return (white_pieces == 0 or black_pieces == 0 or not has_valid_moves)

    def evaluate(self, node: Node) -> float:
        opponent = "W" if self.player == "B" else "B"

        player_count = np.count_nonzero(node.state == self.player)
        opponent_count = np.count_nonzero(node.state == opponent)

        player_moves = node.moves
        opponent_moves = sum(child.moves for child in node.children)

        player_captures = node.captures
        opponent_captures = sum(child.captures for child in node.children)

        # Assign weights to each factor
        piece_weight = 1.0
        move_weight = 0.5
        capture_weight = 2.0

        player_score = (player_count * piece_weight) + (player_moves * move_weight) + (player_captures * capture_weight)
        opponent_score = (opponent_count * piece_weight) + (opponent_moves * move_weight) + (opponent_captures * capture_weight)

        # Normalize between -1 and 1
        total_score = player_score - opponent_score
        max_possible_score = (piece_weight * 20) + (move_weight * 20) + (capture_weight * 20)  # Approximate max values

        return total_score / max_possible_score

    def utility(self, node: Node) -> float:
        if self.is_terminal(node.state, self.player):
            opponent = "W" if self.player == "B" else "B"
            if np.count_nonzero(node.state == self.player) > 0:
                return 1.0 
            elif np.count_nonzero(node.state == opponent) > 0:
                return -1.0
        return 0.0
