import sys
from tukvnanawopi import Tukvnanawopi
from player import Player
import numpy as np


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <board_file> <B|W>")
        return

    board_file = sys.argv[1]
    player_char = sys.argv[2].upper()
    if player_char not in ('B', 'W'):
        print("Error: Player must be 'B' or 'W'")
        return

    with open(board_file, 'r') as f:
        board_state = [list(line.strip().split()) for line in f.readlines()]
    
    board_state = np.array(board_state, dtype=str)

    state_separated = np.array([list(cell[0]) for cell in board_state])

    player = Player.BLACK if player_char == 'B' else Player.WHITE
    game = Tukvnanawopi(player=player, time_limit=10, state=state_separated)

    # print("Initial Board:")
    # print(state_separated)
    # game.root.possible_states()
    # print(f"Possible moves: {game.root.moves}")
    # print(f"Capture moves: {game.root.captures}")
    # #print(game.root.children)

    evaluation, best_move = game.minimax(game.root, depth=10, maximizing_player=True)
    print("Best move is:", best_move, evaluation)


if __name__ == "__main__":
    main()
    
