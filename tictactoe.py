"""
Tic Tac Toe Player
"""

import math
import copy
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

#board = initial_state() # testing purposes

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # If there is an even amount of emtpy spaces it is O's turn
    # If there is an odd amount of empty spaces it is X's turn
    space_counter = 0
    for i in board:
        for spaces in i:
            if spaces == None:
                space_counter += 1
    if space_counter % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    combinations = set()
    for i, row in enumerate(board): # rows
        for j, col in enumerate(row): # columns
            if board[i][j] not in ["X", "O"]:
                coord = (i, j)
                combinations.add(coord)
    return combinations


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("This move is invalid")
    reslt = copy.deepcopy(board)
    reslt[action[0]][action[1]] = player(board)
    return reslt



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] in ['O', 'X']:
            return row[0] # returning X or O, whatever player it is
    
    # Verticals
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] in ['O', 'X']:
            return board[0][i]
    
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ['O', 'X']:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] in ['O', 'X']:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game_result = winner(board)
    if game_result == O or game_result == X:
        return True
    check = 0
    for i in board:
        for j in i:
            if j == EMPTY:
                check += 1
    if check == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    checker = winner(board)
    if checker == X:
        return 1
    elif checker == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            most_optimal = -math.inf # starting value
            for action in actions(board):
                v = min_value(result(board, action))
                if v > most_optimal:
                    most_optimal = v
                    best_action = action # we can return this value in (i, j) format
        else:
            most_optimal = math.inf # starting value
            for action in actions(board):
                v = max_value(result(board, action))
                if v < most_optimal: # we just do the reverse of the min_value()
                    most_optimal = v
                    best_action = action # we can return this value in (i, j) format
    return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf # you know you can always do better than this
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


# backwards of max_value
def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf # you can always do worse than this
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
