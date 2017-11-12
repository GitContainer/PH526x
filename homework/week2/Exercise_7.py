"""
Create a similar function col_win(board, player) that takes the player (integer), and determines
if any column consists of only their marker. Have it return True if this condition is met, and False otherwise.
board is already defined from previous exercises. Call col_win to check if Player 1 has a complete column.
"""
import numpy as np

from homework.week2.Exercise_5 import board


def col_win(board, player):
    for j in range(board.shape[1]):
        if np.all(board[:, j] == player):
            return True
    return False


col_win(board, 1)
