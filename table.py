class Table:
    def __init__(self, width=5, hight=5):
        self.width = width
        self.hight = hight

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.hight
