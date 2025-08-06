"""
Tic Tac Toe Game in Python. There is an ASCII board and two players take turns selecting a square on the board on the command line. The game checks for a win or a draw after each move.

Usage:
    python tic-tac-toe.py
"""

import random

# Define the board state
def create_board():
    return {
        "A": "A", "B": "B", "C": "C",
        "D": "D", "E": "E", "F": "F",
        "G": "G", "H": "H", "J": "J"
    }

# Define a function to keep track of who owns what space
# True = X (Player 1), False = O (Player 2), None = not taken
def create_occupied():
    return {pos: None for pos in [
        "A", "B", "C",
        "D", "E", "F",
        "G", "H", "J"
    ]}

# Winning combinations (rows, columns, diagonals)
winning_combinations = [
    # Rows
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "J"],
    # Columns
    ["A", "D", "G"],
    ["B", "E", "H"],
    ["C", "F", "J"],
    # Diagonals
    ["A", "E", "J"],
    ["C", "E", "G"]
]

# Define a function to print the board on the console
def print_board(board):
    print()
    print(f"{board['A']} | {board['B']} | {board['C']}")
    print("---+----+---")
    print(f"{board['D']} | {board['E']} | {board['F']}")
    print("---+----+---")
    print(f"{board['G']} | {board['H']} | {board['J']}")
    print()

# Define a function to check for a winning combination
def check_winner(occupied):
    for combo in winning_combinations:
        values = [occupied[pos] for pos in combo]
        if values[0] is not None and all(val == values[0] for val in values):
            return values[0]
    return None

# Define a function to check if the game is a draw
def is_draw(occupied):
    return all(value is not None for value in occupied.values())

# Define a function to repeat the game, if desired
def play_again():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        else:
            print("Please enter 'y' or 'n'.")

# Define the game function
def play_game():

    # Get player names from the command line once
    player1 = input("Enter Player 1 name (X): ").strip()
    player2 = input("Enter Player 2 name (O): ").strip()
    print(f"Welcome to the game, {player1} and {player2}!")
    players = {
        True: {"name": player1, "mark": "X"},
        False: {"name": player2, "mark": "O"}
    }

    # Repeat game from here
    while True:

        # Create the board
        board = create_board()
        occupied = create_occupied()

        # Randomize who goes first
        player_turn = random.choice([True, False])
        print(f"\nFlipping a coin... 🎲 {players[player_turn]['name']} goes first!")

        # Start the game
        print("\nGame start! Use positions like A, E, etc.")
        print_board(board)

        # Play the game
        while True:
            current = players[player_turn]
            move = input(f"{current['name']} ({current['mark']}), choose your move: ").strip().upper()

            if move not in board:
                print("Invalid position. Try again")
                continue
            if occupied[move] is not None:
                print("That space is already taken. Try again.")
                continue

            board[move] = current["mark"]
            occupied[move] = player_turn
            print_board(board)

            winner = check_winner(occupied)
            if winner is not None:
                print(f"{players[winner]['name']} wins! 🏆")
                break

            if is_draw(occupied):
                print("It's a draw! 🤝")
                break

            player_turn = not player_turn

        if not play_again():
            print("Thanks for playing! 👋")
            break

# Run the script
if __name__ == "__main__":
    play_game()