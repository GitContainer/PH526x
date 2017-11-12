"""
Now that players may place their pieces, how will they know they've won?
Make a function row_win(board, player) that takes the player (integer), and determines
if any row consists of only their marker. Have it return True of this condition is met, and False otherwise.
board is already defined from previous exercises. Call row_win to check if Player 1 has a complete row.
"""
import numpy as np

from homework.week2.Exercise_5 import board


def row_win(board, player):
    for i in range(board.shape[0]):
        if np.all(board[i] == player):
            return True
    for j in range(board.shape[1]):
        if np.all(board[:, j] == player):
            return True
    return False


print(row_win(board, 1))
