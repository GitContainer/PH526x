"""
Write a function random_place(board, player) that places a marker for the current player at random among all the
available positions (those currently set to 0). a. Find possible placements with possibilities(board). b.
Select one possible placement at random using random.choice(selection).
board is already defined from previous exercises. Call random_place(board, player) to place a random marker
for Player 2, and store this as board to update its value.
"""
import random

from week2 import possibilities, board


def random_place(board, player):
    board[random.choice(possibilities(board))] = player


random_place(board, 2)

print(board)
