"""
For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3.
Make a function create_board() that creates such a board, with values of integers 0.
Call create_board(), and store this as board
"""

import numpy as np


def create_board():
    return np.zeros((3, 3))


board = create_board()

print(board)
