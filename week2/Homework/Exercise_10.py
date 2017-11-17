"""
create_board(), random_place(board, player), and evaluate(board) have been created from previous exercises.
Create a function play_game() that creates a board, calls alternates between two players (beginning with Player 1),
and evaluates the board for a winner after every placement. Play the game until one player wins (returning 1 or 2
to reflect the winning player), or the game is a draw (returning -1).
Call play_game once.
"""
from week2 import create_board
from week2 import evaluate
from week2 import random_place


def play_game():
    board = create_board()
    for player in [1, 2]:
        random_place(board, player)
        evaluate(board)


play_game()
