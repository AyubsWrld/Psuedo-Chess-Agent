import sys
from tukvnanawopi import Tukvnanawopi
from player import Player


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

    player = Player.BLACK if player_char == 'B' else Player.WHITE
    game = Tukvnanawopi(player=player, time_limit=10, state=board_state)

    print("Initial Board:")
    print(board_state)


if __name__ == "__main__":
    main()
