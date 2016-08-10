# This is based on a coding exercise from CodeAcademy

from random import randint

def create_board():
    """Create 5 x 5 board with letter "O" in each position."""
    board = []
    for x in range(5):
        board.append(["O"] * 5)
    return board

def print_board(board):
    """Print board without quotation marks."""
    for row in board:
        print " ".join(row)

def random_row(board):
    """Get a random row from the board."""
    return randint(0, len(board) - 1)

def random_col(board):
    """Get a random column from the board."""
    return randint(0, len(board[0]) - 1)

def play_game():
    """Play the battleship game.
    Allow a maximum of 4 turns.
    End game if user selects the randomly selected target position.
    """
    # Create and print board at beginning of game
    board = create_board()
    print "Let's play Battleship!"
    print_board(board)
    print

    # Set the ship's target position
    ship_row = random_row(board)
    ship_col = random_col(board)

    # Allow the user 4 turns to guess the target position
    for turn in range(4):
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"

            if turn == 3:
                print "Game Over"
            # Print (turn + 1) here!
            print
            print "Turn", turn + 1
            print_board(board)
            print

play_game()