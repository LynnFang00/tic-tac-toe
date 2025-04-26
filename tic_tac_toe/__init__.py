"""
Tic-Tac-Toe Game with AI Opponent using Minimax Algorithm and Alpha-Beta Pruning
"""

# ---------------------------------------------------------------------------
# Public constants expected by the tests
# ---------------------------------------------------------------------------

X = "X"          # human
O = "O"          # AI
EMPTY = " "      # blank square

__all__ = [
    "X", "O", "EMPTY",
    "print_board",
    "check_win",
    "is_draw",
    "get_available_moves",
    "minimax",
    "get_ai_move",
]


def print_board(board):
    """Display the current game board in a human-readable format.

    Args:
        board (list): 3x3 list representing the game board
    """
    for i, row in enumerate(board):
        # Join elements with vertical separators
        print(" " + " | ".join(row))
        # Add horizontal separators between rows
        if i < 2:
            print("-----------")


def check_win(board, player):
    """Check if the specified player has a winning configuration.

    Args:
        board (list): Current game board
        player (str): 'X' or 'O' to check for win

    Returns:
        bool: True if player has won, False otherwise
    """
    # Check all rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Horizontal check
            return True
        if all(board[j][i] == player for j in range(3)):  # Vertical check
            return True
    # Check both diagonals
    diagonal1 = all(board[i][i] == player for i in range(3))  # Top-left to bottom-right
    diagonal2 = all(board[i][2 - i] == player for i in range(3))  # Top-right to bottom-left
    return diagonal1 or diagonal2


def is_draw(board):
    """Check if the game has reached a draw state (no empty cells).

    Args:
        board (list): Current game board

    Returns:
        bool: True if board is full with no winner, False otherwise
    """
    return all(cell != ' ' for row in board for cell in row)


def get_available_moves(board):
    """Identify all legal moves remaining on the board.

    Args:
        board (list): Current game board

    Returns:
        list: Tuple coordinates (row, col) of empty cells
    """
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']


def minimax(board, alpha, beta, is_maximizing):
    """Minimax algorithm with Alpha-Beta pruning to evaluate board states.

    Args:
        board (list): Current game board
        alpha (float): Best already explored value for maximizer
        beta (float): Best already explored value for minimizer
        is_maximizing (bool): True if current player is maximizing (AI)

    Returns:
        int: Score of the board state (1 for AI win, -1 for player win, 0 for draw)
    """
    # Base case: Terminal state reached
    if check_win(board, 'O'):
        return 1  # AI wins
    if check_win(board, 'X'):
        return -1  # Human wins
    if is_draw(board):
        return 0  # Draw

    if is_maximizing:
        max_score = -float('inf')
        for move in get_available_moves(board):
            # Simulate AI move
            board[move[0]][move[1]] = 'O'
            # Recursively evaluate position
            score = minimax(board, alpha, beta, False)
            # Undo move for next simulation
            board[move[0]][move[1]] = ' '

            max_score = max(max_score, score)
            alpha = max(alpha, score)
            # Alpha-Beta pruning condition
            if beta <= alpha:
                break  # Stop exploring this branch
        return max_score
    else:
        min_score = float('inf')
        for move in get_available_moves(board):
            # Simulate human move
            board[move[0]][move[1]] = 'X'
            score = minimax(board, alpha, beta, True)
            board[move[0]][move[1]] = ' '

            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  # Prune this branch
        return min_score


def get_ai_move(board):
    """Determine the optimal move for the AI using Minimax evaluation.

    Args:
        board (list): Current game board

    Returns:
        tuple: (row, col) coordinates for best move
    """
    best_score = -float('inf')
    best_move = None

    # Evaluate all possible moves
    for move in get_available_moves(board):
        # Test the move
        board[move[0]][move[1]] = 'O'
        # Get minimax score assuming optimal play
        score = minimax(board, -float('inf'), float('inf'), False)
        # Reset the board
        board[move[0]][move[1]] = ' '

        # Update best move
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def main():
    """Main game loop handling player input and game state management."""
    # Initialize empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe against AI!")
    print("You're X, AI is O. Let's begin!\n")
    print_board(board)

    while True:
        # Human player's turn
        while True:
            try:
                # Get and validate input
                row = int(input("\nEnter row (0-2): "))
                col = int(input("Enter column (0-2): "))

                # Check valid coordinates and empty cell
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                # Error messages
                print("Invalid move. Try again." if board[row][col] != ' '
                      else "Coordinates must be 0-2!")
            except (ValueError, IndexError):
                print("Please enter numbers 0, 1, or 2!")

        # Display updated board
        print("\nYour move:")
        print_board(board)

        # Check game state after human move
        if check_win(board, 'X'):
            print("\nCongratulations! You won!")
            break
        if is_draw(board):
            print("\nIt's a draw!")
            break

        # AI's turn - calculate and make optimal move
        ai_row, ai_col = get_ai_move(board)
        board[ai_row][ai_col] = 'O'
        print(f"\nAI plays at ({ai_row}, {ai_col}):")
        print_board(board)

        # Check game state after AI move
        if check_win(board, 'O'):
            print("\nAI wins! Better luck next time!")
            break
        if is_draw(board):
            print("\nIt's a draw!")
            break


if __name__ == "__main__":
    # Start the game when script is run
    main()
