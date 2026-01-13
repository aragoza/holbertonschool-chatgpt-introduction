#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("--+---+--")


def check_wwinner(board):
    """
    Check if there is a winner on the board.

    Returns True if a player has won, otherwise False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def get_valid_input(player, name):
    """
    Ask for a valid integer input (0,1,2).
    Handles chars, negatives, out of range inputs.
    """
    while True:
        value = input(f"Enter {name} (0, 1, or 2) for player {player}: ")
        if not value.isdigit():
            print("Invalid input! Please enter a number (0, 1, or 2).")
            continue

        value = int(value)

        if 0 <= value <= 2:
            return value
        else:
            print("Number out of range! Please enter 0, 1, or 2.")


def tic_tac_toe():
    """
    Main function to play Tic-Tac-Toe between two players.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # validated input for row & col
        row = get_valid_input(player, "row")
        col = get_valid_input(player, "column")

        if board[row][col] == " ":
            board[row][col] = player
            if check_wwinner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")


# Start the game
tic_tac_toe()