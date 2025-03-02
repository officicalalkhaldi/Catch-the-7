import random


class Player:
    def __init__(self, row, col, symbol):
        self.row = row
        self.col = col
        self.symbol = symbol


class Player7(Player):
    def __init__(self, row, col):
        super().__init__(row, col, "7")

    def move(self, grid):
        valid_move = False
        while not valid_move:
            direction = random.choice(["up", "down", "left", "right"])
            steps = random.choice([1, 2])
            new_row, new_col = self.row, self.col

            if direction == "up":
                new_row -= steps
            elif direction == "down":
                new_row += steps
            elif direction == "left":
                new_col -= steps
            elif direction == "right":
                new_col += steps

            if grid.is_valid(new_row, new_col):
                valid_move = True
                self.row, self.col = new_row, new_col


class Player2(Player):
    def __init__(self, row, col):
        super().__init__(row, col, "2")

    def move_toward(self, target_row, target_col, grid):

        new_row, new_col = self.row, self.col

        if self.row < target_row and grid.is_valid(self.row + 1, self.col):
            new_row += 1
        elif self.row > target_row and grid.is_valid(self.row - 1, self.col):
            new_row -= 1

        if self.col < target_col and grid.is_valid(new_row, self.col + 1):
            new_col += 1
        elif self.col > target_col and grid.is_valid(new_row, self.col - 1):
            new_col -= 1

        self.row, self.col = new_row, new_col
