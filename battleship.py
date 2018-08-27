"""Battleship game"""
from random import randint
board = []
for row in range(5):
    board.append(["O"] * 5)

def print_board(board_in):
    for row in board_in:
        print(" ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board) -1)

def random_col(board):
    return randint(0, len(board) -1)

# Get a random row and column where the ship is hidden
ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print('Turn ' + str(turn + 1))
    #Get the user's guess of the row and column where the ship is hidden
    guess_row = int(input('Guess Row: '))
    guess_col = int(input('Guess Col: '))

    if guess_row == ship_row and guess_col == ship_col:
        print('Congratulations! You sank my battleship')
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == 'x':
            print('You guessed that one already')
        else:
            print('You missed my battleship!')
            board[guess_row][guess_col] = "x"
        print_board(board)
        if (turn == 3):
            print('Game over')
            print_board(board)
