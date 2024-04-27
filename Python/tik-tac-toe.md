# Define the game board
board = [' ' for _ in range(9)]  # List of 9 empty spaces

# Define functions
def print_board(board):
  """Prints the current state of the game board."""
  for i in range(3):
    for j in range(3):
      print(board[i*3 + j], end=' ')
    print()  # Print newline after each row

def is_winner(board, player):
  """Checks if a player has won the game."""
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                    (0, 4, 8), (2, 4, 6))  # Diagonals
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False

def is_board_full(board):
  """Checks if all spaces on the board are filled."""
  return ' ' not in board

def get_player_move(board):
  """Gets a valid move from the current player."""
  while True:
    try:
      move = int(input("Enter your move (1-9): ")) - 1
      if 0 <= move <= 8 and board[move] == ' ':
        return move
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 9.")

def play():
  """Main game loop."""
  current_player = 'X'  # Start with player X
  while True:
    print_board(board)
    move = get_player_move(board)
    board[move] = current_player

    if is_winner(board, current_player):
      print(f"Player {current_player} wins!")
      break
    elif is_board_full(board):
      print("It's a tie!")
      break

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play()
