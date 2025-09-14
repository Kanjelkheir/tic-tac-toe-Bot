"""
Tic Tac Toe Player
"""

import math
from typing import Set, Tuple

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    amount_of_x = 0
    amount_of_o = 0

    for i in board:
        for j in i:
            if j == X:
                amount_of_x += 1
            if j == O:
                amount_of_o += 1

    if amount_of_o < amount_of_x:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    #store all the possible moves (row, column) in a set
    result = set()

    for row_index,row in enumerate(board):
        for column_index, column in enumerate(row):
            if column is EMPTY:
                result.add((row_index, column_index))

    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #validate the indices
    if action[0] > 2 or action[0] < 0:
        raise Exception("Invalid index")

    #get the current player
    current_player = player(board)

    #make a deep copy of the board
    import copy
    new_board = copy.deepcopy(board)

    #destructure the index from the action
    i, j = action

    #apply the action on the copy of the board
    new_board[i][j] = current_player

    #return the copy of the board
    return new_board



def check_three(a, b, c):
    """
    Helper function to check if three cells are the same and not EMPTY.
    """
    if a is not EMPTY and a == b and a == c:
        return a
    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check rows
    for i in range(3):
        w = check_three(board[i][0], board[i][1], board[i][2])
        if w:
            return w

    #check columns
    for j in range(3):
        w = check_three(board[0][j], board[1][j], board[2][j])
        if w:
            return w

    #check diagonals
    w = check_three(board[0][0], board[1][1], board[2][2])
    if w:
        return w

    w = check_three(board[0][2], board[1][1], board[2][0])
    if w:
        return w

    #if no winner, check if there are any empty cells
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return None

    #no winner - tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # get the game winner
    game_winner = winner(board)

    match game_winner:
        case 'X':
            return 1
        case 'O':
            return -1
        case _:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_val_result = min_value(result(board, action))
            if min_val_result > v:
                v = min_val_result
                best_action = action
        return best_action
    else:
        v = math.inf
        best_action = None
        for action in actions(board):
            max_val_result = max_value(result(board, action))
            if max_val_result < v:
                v = max_val_result
                best_action = action
        return best_action


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
