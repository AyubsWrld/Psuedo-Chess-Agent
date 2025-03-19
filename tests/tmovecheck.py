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
   
    if player_char not in ('B', 'W'):
        print("Error: Player must be 'B' or 'W'")
        return
    
    if not os.path.exists(board_file):
        print(f"Could not resolve file: '{board_file}'")
        return
    
    with open(board_file, 'r') as f:
        board_state = [line.strip() for line in f.readlines()]
    
    # Print the board in the desired format
    print_board(board_state)

def print_board(board):
    # Print column headers
    print("  ABCDEFGHI")
    
    # Print each row with row numbers
    for i in range(len(board)):
        row_num = 9 - i  # Start from 9 and go down to 1
        row = board[i]
        
        # Print row number at the beginning
        print(f"{row_num} ", end="")
        
        # Print each character in the row without extra spaces
        row_content = ''.join(row.replace('X', ' '))
        print(row_content, end=" ")
        
        # Print row number at the end
        print(row_num)
    
    # Print column headers again at the bottom
    print("  ABCDEFGHI")

if __name__ == "__main__":
    main()
