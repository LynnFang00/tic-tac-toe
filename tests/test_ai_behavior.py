"""
Unit tests for get_ai_move + minimax core behaviour.
"""

from tic_tac_toe import get_ai_move, minimax, check_win


def board_from_strings(rows):
    return [[c if c in "XO" else " " for c in row] for row in rows]


# AI first move should be corner or center ---------------------------------

def test_ai_first_move_corner_or_center():
    board = board_from_strings([
        "   ",
        "   ",
        "   ",
    ])
    move = get_ai_move(board)
    assert move in {(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)}


# AI takes immediate win when available -----------------------------------

def test_ai_takes_winning_move():
    board = board_from_strings([
        "OO ",
        "XX ",
        "X  ",
    ])
    move = get_ai_move(board)
    # After playing, AI should win
    board[move[0]][move[1]] = "O"
    assert check_win(board, "O")


# Optional: minimax score symmetry (quick) --------------------------------

def test_minimax_symmetric_scores():
    """
    Verifies that score from AI's perspective is negation of score
    from human perspective in same position.
    """
    from tic_tac_toe import minimax
    board = board_from_strings([
        "X  ",
        " O ",
        "   ",
    ])

    score_ai_turn = minimax(board, -float("inf"), float("inf"), is_maximizing=False)
    # Flip turn: treat current board as if AI is 'X' (maximizing)
    score_human_turn = minimax(board, -float("inf"), float("inf"), is_maximizing=True)

    assert score_ai_turn == -score_human_turn
