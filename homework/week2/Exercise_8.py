"""
Finally, create a function diag_win(board, player) that tests if either diagonal of the board
consists of only their marker. Have it return True if this condition is met, and False otherwise.
board is already defined from previous exercises. Call diag_win to check if Player 1 has a complete diagonal.
"""
import numpy as np

from homework.week2.Exercise_5 import board


def diag_win(board, player):
    if np.all(board.diagonal() == player):
        return True
    return False


print(diag_win(board, 1))
