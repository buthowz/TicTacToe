"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None
min_moves = []
max_moves = []
moves = []
O_Move = ()
X_Move = ()


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
    # initial state, X turn
    firstTurn = True
    oCount = 0
    xCount = 0

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != EMPTY:
                firstTurn = False
            if board[r][c] == X:
                xCount += 1
            if board[r][c] == O:
                oCount += 1
    if firstTurn:
        #print("I_X")
        return X
    elif xCount > oCount:
        #print("O")
        return O
    elif oCount == xCount:
        #print("X")
        return X


def actions(board):
    """
    Returns set of all possible actions (i=r, j=c) available on the board.
    """
    possibleActions = set()
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == EMPTY:
                action = (r, c)
                possibleActions.add(action)
    return possibleActions
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # suppose action is (i, j, X or O), e.g if played by X, (i, j, X)
    # action is a tuple of (row, col, Player)
    row = action[0]
    col = action[1]
    if (board[row][col] is not EMPTY):
        raise ("Choose an empty spot!!")
    newBoard = copy.deepcopy(board)
    play = player(board) # gets whoever's turn it is
    newBoard[row][col] = play

    return newBoard
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        winner = utility(board)
        if winner == 0:
            return None
        elif winner == -1:
            return O
        elif winner == 1:
            return X
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (utility(board) == 1 or utility(board) == -1):
        return True

    # end game if there is only one move left
    # means there is no possibility of winning
    #elif (countEmpty(board) == 1):

    # there is no empty spot left, means game over
    elif (countEmpty(board) == 0):
        return True
    else:
        return False
    #raise NotImplementedError

def countEmpty(board):
    count = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == EMPTY:
                count += 1
    return count

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    x_win = utility_helper(board, X)
    if (x_win):
        return 1
    o_win = utility_helper(board, O)
    if (o_win):
        return -1
    else:
        return 0

def utility_helper(board, player):
    """
    Checks winner by checking rows, columns and diagonals
    Checks if they have same consecutive player
    """
    boardLength = len(board)
    for r in range(boardLength):
        row_values = []
        col_values = []
        diag1_values = []
        diag2_values = []
        row_win = False
        col_win = False
        diag1_win = False
        diag2_win = False
        for c in range(boardLength):
            # getting row and column values
            row_values.append(board[r][c])
            col_values.append(board[c][r])

            # getting diagonals' values
            if (r == 0): # get values only if first column
                diag1_values.append(board[c][c])
            if (r == boardLength - 1): # get values only if last column
                diag2_values.append(board[c][r-c])

        # Check if there is a winner
        row_win = player_won(row_values, player)
        col_win = player_won(col_values, player)
        if r == 0:
            diag1_win = player_won(diag1_values, player)
        if r == boardLength - 1:
            diag2_win = player_won(diag2_values, player)

        # if one of these are True we found a winner
        if (row_win or col_win or diag1_win or diag2_win):
            return True

    # no winner
    return False

def player_won(values, player):
    """
    values = [x, x, x], player = x
    returns True
    """
    for i in values:
        if i != player:
            return False
    return True


def minimax(board):
    if terminal(board):
        return None
    current_player = player(board)
    possible_actions = actions(board)
    for action in possible_actions:
        newBoard = result(board, action)
        if current_player == O:
            worst_v = 1
            o_v = max_value(newBoard)
            if (o_v < worst_v):
                worst_v = o_v
                moves.insert(0, action)
        elif current_player == X:
            worst_v = -1
            x_v = min_value(newBoard)
            if (x_v > worst_v):
                worst_v = x_v
                moves.insert(0, action)
    return moves.pop(0)

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    
    possible_actions = actions(board)
    for action in possible_actions:
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    
    possible_actions = actions(board)
    for action in possible_actions:
        v = min(v, max_value(result(board, action)))
    return v
