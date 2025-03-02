import sys

from code.grid import Grid
from code.players import Player2, Player7


class Game:
    def __init__(self, grid_size=8):
        self.grid = Grid(grid_size)
        self.player7 = Player7(1, 1)
        self.player2 = Player2(5, 6)
        self.turn = 0

    def print_grid(self):

        sys.stdout.write("\033[H")
        sys.stdout.write("\033[J")

        print("          Welcome to Catch the 7\n")
        print("  ------------------------------------------\n")

        for row in range(1, self.grid.size + 1):
            row_str = f"     {row}| "
            for col in range(1, self.grid.size + 1):

                cell = "0"
                if row == self.player7.row and col == self.player7.col:
                    cell = "\033[95m7\033[0m"
                elif row == self.player2.row and col == self.player2.col:
                    cell = "\033[91m2\033[0m"
                row_str += f"\033[48;5;236m {cell} \033[0m "
            print(row_str)

        print("\n  ------------------------------------------")
        print(f"\n  [-] turn : {self.turn + 1}")
        print(f"  [-] Player2 position: ({self.player2.row}, {self.player2.col})")
        print("  [-] white : 0")
        print("  [-] black : 0")

    def is_caught(self):
        return (
            self.player2.row == self.player7.row
            and self.player2.col == self.player7.col
        )

    def play(self):
        max_turns = 20

        sys.stdout.write("\033[H\033[J")
        self.print_grid()

        while not self.is_caught() and self.turn < max_turns:

            while True:
                print(
                    "\n  [-] input : [squares] [direction] (e.g., '2 u' for 2 squares up)"
                )
                print("  Directions: 'u' (up), 'd' (down), 'l' (left), 'r' (right)")
                try:
                    move_input = input("  Enter your move: ").strip().lower().split()
                    if len(move_input) != 2:
                        print(
                            "Invalid input! Please enter in the format '[squares] [direction]'."
                        )
                        continue

                    squares = int(move_input[0])
                    direction = move_input[1]

                    if direction not in ["u", "d", "l", "r"]:
                        print(
                            "Invalid direction! Use 'u' (up), 'd' (down), 'l' (left), or 'r' (right)."
                        )
                        continue

                    new_row, new_col = self.player2.row, self.player2.col

                    if direction == "u":
                        new_row -= squares
                    elif direction == "d":
                        new_row += squares
                    elif direction == "l":
                        new_col -= squares
                    elif direction == "r":
                        new_col += squares

                    if self.grid.is_valid(new_row, new_col):
                        self.player2.row, self.player2.col = new_row, new_col
                        break
                    else:
                        print("Invalid move! You can't go out of bounds.")
                except ValueError:
                    print("Invalid input! Number of squares must be a number.")
                except KeyboardInterrupt:
                    print("\nGame interrupted. Exiting...")
                    return

            if self.is_caught():
                break

            print("\nPlayer7 (7) is moving...")
            self.player7.move(self.grid)

            self.print_grid()

            self.turn += 1

        print("\nGame Over!")
        self.print_grid()

        if self.is_caught():
            print(f"You caught Player7 in {self.turn + 1} turns! You win!")
        else:
            print(f"Player7 escaped for {max_turns} turns. You lose!")
