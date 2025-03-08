import time
from player import Player
import minimax
import numpy as np


class Tukvnanawopi:
    def __init__(self, player: Player, time_limit: float, state):
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
        # check is a move is possible, given the state of the board, rows of the player, and columns of the player
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
                new_state[rows[count] - 1, cols[count] - 1] = "R"
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

    def is_terminal(self, state, player: Player) -> bool:
        # is end of game
        return

    def evaluate(self, state) -> float:
        # heuristic
        return

    def utility(self, state) -> int:
        # -1, 0 or 1
        return
