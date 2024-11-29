import math

# Display the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

# Check if there are moves left on the board
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Evaluate the board to check for winner
def evaluate(board):
    # Check rows for victory
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return 10 if row[0] == "X" else -10
    
    # Check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == "X" else -10
    
    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "X" else -10
    
    return 0

# Minimax algorithm with optional Alpha-Beta Pruning
def minimax(board, depth, is_maximizing_player):
    score = evaluate(board)
    
    # If AI or human wins, return score
    if score == 10 or score == -10:
        return score
    
    # If no more moves, it's a draw
    if not is_moves_left(board):
        return 0
    
    # Maximizing player's move (AI)
    if is_maximizing_player:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, not is_maximizing_player))
                    board[i][j] = " "
        return best
    
    # Minimizing player's move (Human)
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, not is_maximizing_player))
                    board[i][j] = " "
        return best

# Find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Main game loop
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', and the AI is 'X'. Make your move by entering row and column (1-3).")
    
    print_board(board)
    
    while True:
        # Human player's turn
        while True:
            try:
                move = input("Enter your move (row and column, e.g., 1 2): ").split()
                row, col = int(move[0]) - 1, int(move[1]) - 1
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 1 and 3.")
        
        print_board(board)
        
        # Check if human won
        if evaluate(board) == -10:
            print("Congratulations! You won!")
            break
        
        # Check if it's a draw
        if not is_moves_left(board):
            print("It's a draw!")
            break
        
        # AI's turn
        print("AI is making its move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print_board(board)
        
        # Check if AI won
        if evaluate(board) == 10:
            print("AI wins! Better luck next time.")
            break
        
        # Check if it's a draw
        if not is_moves_left(board):
            print("It's a draw!")
            break

# Start the game
play_tic_tac_toe()
