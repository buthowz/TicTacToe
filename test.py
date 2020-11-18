from tictactoe import initial_state, player, actions, result, winner, terminal, max_value, min_value, minimax

X = "X"
O = "O"
EMPTY = None

def main():
    print("Initial State testing: ")
    player(initial_state()) # prints I_X, means first turn for X
    print("Testing O's Turn: ")
    board = [[O, X, EMPTY],   # at this moment O's turn, as O and X counts are equal
            [EMPTY, EMPTY, X],
            [O, X, EMPTY]]
    player(board)
    print("All possible Actions in empty board: ")
    print(actions(initial_state()))

    #print("Result Testing: Player X moves at (1, 2)")
    #print(result(initial_state(), (1, 2, X)))

    board1 = [[O, X, O],   # at this moment X wins the game
            [EMPTY, X, X],
            [X, X, EMPTY]]
    print("Winner Testing: X wins this game")
    print(winner(board1))

    board2 = [[O, EMPTY, O],   # at this moment O wins the game
            [X, O, X],
            [O, X, X]]
    print("Winner Testing: O wins this game")
    print(winner(board2))

    board3 = [[X, O, O],
            [O, X, X],
            [X, X, O]]
    print("Winner Testing: Game Drawn")
    print(winner(board3))

    print("Testing game terminal: ")
    print("Prints True:")
    print(terminal(board1) and terminal(board2))

    board4 = [[O,   X,      O],
            [EMPTY, EMPTY,  X],
            [X,     O,      EMPTY]]

    print("Prints False:")
    print(terminal(board4))

    board5 = [[EMPTY, X,    O],
            [EMPTY,   X,    O],
            [EMPTY,   EMPTY, EMPTY]]
    print("\nTest Max_value: prints(2, 1)")
    #print(max_value(board5))

    
    board6 = [[EMPTY, X, O],
            [X, X, EMPTY],
            [EMPTY, O, EMPTY]]
    print("\nTest Min_value: prints(1, 2)")
    #print(min_value(board6))


    
    print("\nMinimax Test: print(1, 2)")
    #print('Minmax move: ', minimax(board6))

    board7 = [[EMPTY, X, O],
            [X, X, EMPTY],
            [EMPTY, O, EMPTY]]

    board8 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    print("\nMinimax Test: print(1, 0)")
    print('Minmax move: ', minimax(board8))

    board9 = [[EMPTY, EMPTY, EMPTY],
            [X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    print("\nMinimax Test: print something")
    #print('Minmax move: ', minimax(board9))





main()
