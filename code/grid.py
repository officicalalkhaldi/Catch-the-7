class Grid:
    def __init__(self, size=5):
        self.size = size

    def is_valid(self, row, col):
        return 1 <= row <= self.size and 1 <= col <= self.size
