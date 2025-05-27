from direction import Direction
from position import Position
from table import Table

class Robot:
    def __init__(self, table: Table):
        self.table = table
        self.position: Position = None
        self.direction: Direction = None
        self.is_placed = False

    def place(self, x: int, y: int, direction: Direction):
        if self.table.is_valid_position(x, y):
            self.is_placed = True
            self.position = Position(x, y)
            self.direction = direction

    def move(self):
        if not self.is_placed:
            return

        dx, dy = {
            Direction.NORTH: (0, 1),
            Direction.SOUTH: (0, -1),
            Direction.EAST: (1, 0),
            Direction.WEST: (-1, 0),
        }[self.direction]

        new_x = self.position.x + dx
        new_y = self.position.y + dy

        if self.table.is_valid_position(new_x, new_y):
            self.position = Position(new_x, new_y)

    def turn_left(self):
        if self.is_placed:
            self.direction = Direction.left(self.direction)

    def turn_right(self):
        if self.is_placed:
            self.direction = Direction.right(self.direction)

    def report(self):
        if self.is_placed:
            return f"{self.position.x},{self.position.y},{self.direction.name}"
        return None
