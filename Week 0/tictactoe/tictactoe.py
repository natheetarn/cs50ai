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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    if board == initial_state():
        return X
    x_count=0
    o_count=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count+=1
            if board[i][j] == O:
                o_count +=1
    if(x_count>o_count):
        return O
    elif (x_count==o_count):
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    return moves

    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] == X or board[action[0]][action[1]] == O or action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise actionError('Invalid Action')

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board
    




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]!=EMPTY:
            if board[i][0] == board[i][1] and board[i][2] == board[i][1]:
                return board[i][0]
    for i in range(3):
        if board[0][i]!=EMPTY:
            if board[0][i] == board[1][i] and board[2][i] == board[1][i]:
                return board[0][i];
    if board[0][0] == board[1][1] and board[2][2] == board[1][1]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[2][0] ==  board[1][1]:
        return board[0][2]
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    

def MIN_VAL(board):

    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    move = None
    for action in actions(board):
        tmp, act = MAX_VAL(result(board, action))
        if tmp < v:
            v = tmp
            move = action
            if v == -1:
                return v, move
    
    return v, move

        

def MAX_VAL(board):

    if terminal(board):
        return utility(board),None

    v = float('-inf')
    move = None
    for action in actions(board):
        tmp, act = MIN_VAL(result(board, action))
        if tmp > v: 
            v = tmp
            move = action
            if v == 1:
                return v, move
    
    return v, move

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = MAX_VAL(board)
            return move
        else:
            value, move = MIN_VAL(board)
            return move
