import sys
import os

def main(): 
    if len(sys.argv) != 4:
        print("Usage: tmovecheck file player move ")
        print("""Where: file is the name of a file that contains the board configuration
       player is either B or W, indicating which player the agent should assume
       move is the move the player intends to execute""")
        return
    
    board_file = sys.argv[1]
    player_char = sys.argv[2].upper()
    move_str = sys.argv[3].upper()

    if player_char not in ('B', 'W'):
        print("Error: Player must be 'B' or 'W'")
        return
    
    if not os.path.exists(board_file):
        print(f"Could not resolve file: '{board_file}'")
        return
    
    with open(board_file, 'r') as f:
        board_state = [line.strip() for line in f.readlines()]
   
    # For debugging and getting the state b4 actually making the move 
    # print_board(board_state)

    # Parse move here fails sometimes idk y 
    start_pos, end_pos = move_str.split('-')
    start_row, start_col = parse_position(start_pos)
    end_row, end_col = parse_position(end_pos)

    if not is_valid_move(board_state, player_char, start_row, start_col, end_row, end_col):
        print(f"Invalid move: {move_str}")
        return
    
    # Carry out the move here 
    board_state = make_move(board_state, player_char, start_row, start_col, end_row, end_col)
    print_board(board_state)

def parse_position(pos):
    # the representation from column to value 
    col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
    row = 9 - int(pos[1])  # Convert 6 -> 3, 7 -> 2, etc.
    col = col_map[pos[0]]
    return row, col

def is_valid_move(board_state, player_char, start_row, start_col, end_row, end_col):
    if board_state[start_row][start_col] != player_char:
        return False 
    if board_state[end_row][end_col] != 'O':
        return False  
    if abs(start_row - end_row) > 2 or abs(start_col - end_col) > 2:
        return False  
    if abs(start_row - end_row) == 2 or abs(start_col - end_col) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        if board_state[mid_row][mid_col] == player_char or board_state[mid_row][mid_col] == 'O':
            return False  
    return True

def make_move(board_state, player_char, start_row, start_col, end_row, end_col):
    new_board = [list(row) for row in board_state]  
    new_board[end_row][end_col] = player_char
    new_board[start_row][start_col] = 'O'

    if abs(start_row - end_row) == 2 or abs(start_col - end_col) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        new_board[mid_row][mid_col] = 'O'  # Remove captured piece

    return ["".join(row) for row in new_board]

def print_board(board):
    print("  ABCDEFGHI")
    
    for i in range(len(board)): 
        row_num = 9 - i  
        row = board[i]
        
        print(f"{row_num} ", end="")
        print(row.replace('X', ' '), end=" ")
        print(row_num)
    
    print("  ABCDEFGHI")

if __name__ == "__main__":
    main()
