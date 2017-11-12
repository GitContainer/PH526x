"""
Create a function possibilities(board) that returns a list of all positions (tuples) on the board
that are not occupied (0). (Hint: numpy.where is a handy function that returns a list of indexes that meet a condition.)
board is already defined from previous exercises. Call possibilities(board) to see what it returns!
"""

import numpy as np

from homework.week2.Exercise_1 import create_board

board = create_board()


def possibilities(board):
    return np.where(board[board == 0])


possibilities(board)
