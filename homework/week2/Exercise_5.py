"""
board is already defined from previous exercises. Use random_place(board, player)
to place three pieces on board each for players 1 and 2.
Print board to see your result.
"""
from homework.week2.Exercise_1 import create_board
from homework.week2.Exercise_4 import random_place

board = create_board()
for i in range(3):
    for player in [1, 2]:
        random_place(board, player)

print(board)
