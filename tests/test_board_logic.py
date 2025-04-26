"""
Unit tests for check_win, is_draw, and move validation
(using the plain list-of-lists board).
"""

import pytest
from tic_tac_toe import check_win, is_draw, get_available_moves, X, O

# Helper -------------------------------------------------------------------


def board_from_strings(rows):
    """Create a board (list of lists) from list of 3-char strings."""
    return [[c if c in "XO" else " " for c in row] for row in rows]


# Win detection ------------------------------------------------------------

@pytest.mark.parametrize("rows, winner", [
    (["XXX",
      "   ",
      "   "], "X"),            # horizontal
    (["   ",
      "OOO",
      "   "], "O"),
    (["  X",
      "  X",
      "  X"], "X"),            # vertical
    (["X  ",
      " X ",
      "  X"], "X"),            # main diag
    (["  O",
      " O ",
      "O  "], "O"),            # anti diag
])
def test_check_win(rows, winner):
    board = board_from_strings(rows)
    assert check_win(board, winner) is True


# Draw detection -----------------------------------------------------------

def test_is_draw_full_board():
    board = board_from_strings([
        "XOX",
        "XXO",
        "OXO",
    ])
    assert is_draw(board) is True


def test_is_draw_false_when_empty_cells():
    board = board_from_strings([
        "XOX",
        "X O",
        "OX ",
    ])
    assert is_draw(board) is False


# Move availability --------------------------------------------------------

def test_get_available_moves_count():
    board = board_from_strings([
        "XO ",
        " XO",
        "   ",
    ])
    moves = get_available_moves(board)
    assert len(moves) == 5
    # ensure no duplicates
    assert len(moves) == len(set(moves))
