"""
Tic Tac Toe Game in Python. There is an ASCII board and two players take turns selecting a square on the board on the command line. The game checks for a win or a draw after each move.

Usage:
    python tic-tac-toe.py
"""

import random

# Create a class that manages the board state, player info, input/output, and game logic.
class TicTacToeGame:
    def __init__(self):
        self.winning_combinations = [
            ["A", "B", "C"],  # Row 1
            ["D", "E", "F"],  # Row 2
            ["G", "H", "J"],  # Row 3
            ["A", "D", "G"],  # Col 1
            ["B", "E", "H"],  # Col 2
            ["C", "F", "J"],  # Col 3
            ["A", "E", "J"],  # Diagonal 1
            ["C", "E", "G"]   # Diagonal 2
        ]
        self.positions = [
            "A", "B", "C",
            "D", "E", "F",
            "G", "H", "J"
        ]
        self.players = {}
        self.board = {}
        self.occupied = {}
        self.player_turn = True  # True = player 1, False = player 2

    def setup_players(self):
        name1 = input("Enter Player 1 name (X): ").strip()
        name2 = input("Enter Player 2 name (O): ").strip()
        self.players = {
            True: {"name": name1, "mark": "X"},
            False: {"name": name2, "mark": "O"}
        }

    def reset_board(self):
        self.board = {pos: pos for pos in self.positons}
        self.occupied = {pos: None for pos in self.positions}
        self.player_turn = random.choice([True, False])
        print(f"\nFlipping a coin... 🎲 {self.players[self.player_turn]['name']} goes first!")

    def print_board(self):
        b = self.board
        print()
        print(f"{b["A"]} | {b["B"]} | {b["C"]}")
        print("---+----+---")
        print(f"{b["D"]} | {b["E"]} | {b["F"]}")
        print("---+----+---")
        print(f"{b["G"]} | {b["H"]} | {b["J"]}")

    def check_winner(self):
        for combo in self.winning_combinations:
            values = [self.occupied[pos] for pos in combo]
            if values[0] is not None and all(v == values[0] for v in values):
                return values[0]
        return None
    
    def is_draw(self):
        return all(v is not None for v in self.occupied.values())
    
    def get_move(self):
        current = self.players[self.player_turn]
        while True:
            move = input(f"{current['name']} ({current['mark']}), choose your move: ").strip().upper()
            if move not in self.board:
                print("Invalid position. Try again.")
            elif self.occupied[move] is not None:
                print("That space is already taken. Try again.")
            else:
                return move
            
    def play_round(self):
        self.reset_board()
        print("\nGame start! Use positions like A, B, etc.")
        self.print_board()

        while True:
            move = self.get_move()
            mark = self.players[self.player_turn]["mark"]
            self.board[move] = mark
            self.occupied[move] = self.player_turn
            self.print_board()

            winner = self.check_winner()
            if winner is not None:
                print(f"{self.players[winner]['name']} wins! 🏆")
                break
            if self.is_draw():
                print("It's a draw! 🤝")
                break

            self.player_turn = not self.player_turn

    def play_again(self):
        while True:
            answer = input("Play again? (y/n): ").strip().lower()
            if answer in ["y", "yes"]:
                return True
            elif answer in ["n", "no"]:
                return False
            else:
                print("Please enter 'y' or 'n'.")

    def play(self):
        self.setup_players()
        while True:
            self.play_round()
            if not self.play_again():
                print("Thanks for playing! 👋")
                break 

# Run it
if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()