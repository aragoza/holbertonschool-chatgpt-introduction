#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("--+---+--")  # nicer separator


def check_winner(board):
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


def tic_tac_toe():
    """
    Main function to play Tic-Tac-Toe between two players.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
        col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")


# Start the game
tic_tac_toe()
  