"""
Create a function evaluate(board) that uses row_win, col_win, and diag_win functions for both players. If one of them
has won, return that player's number. If the board is full but no one has won, return -1. Otherwise, return 0.
board is already defined from previous exercises. Call evaluate to see if either player has won the game yet.
"""
import numpy as np

from homework.week2.Exercise_5 import board
from homework.week2.Exercise_6 import row_win
from homework.week2.Exercise_7 import col_win
from homework.week2.Exercise_8 import diag_win


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if np.any([row_win(board, player), col_win(board, player), diag_win(board, player)]):
            return player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


evaluate(board)
