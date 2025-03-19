import sys
from tukvnanawopi import Tukvnanawopi
from player import Player
import numpy as np
from utils.logger import log, LogLevel


def main():
    if len(sys.argv) != 3:
        print("Usage: tukvnanawopi file player")
        print("""Where: file is the name of a file that contains the board configuration\n       player is either B or W, indicating which player the agent should assume""")
        return

    board_file = sys.argv[1]
    player_char = sys.argv[2].upper()
    if player_char not in ('B', 'W'):
        print("Error: Player must be 'B' or 'W'")
        return

    with open(board_file, 'r') as f:
        board_state = [list(line.split()) for line in f.readlines()]
    
    board_state = np.array(board_state, dtype=str)
    board_state = np.array([list(cell[0]) for cell in board_state])

    player = Player.BLACK if player_char == 'B' else Player.WHITE
    game = Tukvnanawopi(player=player, time_limit=10, state=board_state)
    #print(game.root.children)

    # print("Initial Board:")
    # print(state_separated)
    game.root.possible_states()
    # print(f"Possible moves: {game.root.moves}")
    # print(f"Capture moves: {game.root.captures}")
    # #print(game.root.children)

    evaluation, best_move = game.minimax(game.root, depth=10, maximizing_player=True)
    # 
    #print("Best move is:", best_move, evaluation)

    print(f'{best_move[0]}-{best_move[1]}')

if __name__ == "__main__":
    main()
    
