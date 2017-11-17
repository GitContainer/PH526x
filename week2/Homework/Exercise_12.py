"""
This result is expected --- when guessing at random, it's better to go first. Let's see if Player 1 can improve
their strategy. create_board(), random_place(board, player), and evaluate(board) have been created from previous
exercises. Create a function play_strategic_game(), where Player 1 always starts with the middle square, and
otherwise both players place their markers randomly.
Call play_strategic_game once.
"""
from week2 import create_board
from week2 import evaluate
from week2 import random_place


def play_strategic_game():
    board, winner = create_board(), 0
    board[1, 1] = 1
    while winner == 0:
        for player in [2, 1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


play_strategic_game()
