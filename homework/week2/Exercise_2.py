"""
Players 1 and 2 will take turns changing values of this array from a 0 to a 1 or 2, indicating the number of the player
who places there. Create a function place(board, player, position) with player being the current player
(an integer 1 or 2), and position a tuple of length 2 specifying a desired location to place their marker.
Only allow the current player to place a piece on the board (change the board position to their number)
if that position is empty (zero).
Use create_board() to store a board as board, and use place to have Player 1 place a piece on spot (0, 0).
"""
# write your code here!
from homework.week2.Exercise_1 import create_board

board = create_board()


def place(board, player, position):
    board[position[0], position[1]] = player


place(board, 1, (0, 0))
