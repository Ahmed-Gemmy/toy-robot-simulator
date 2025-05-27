from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @classmethod
    def left(cls, current):
        """Rotate the direction 90 degrees to the left (counter-clockwise)."""
        return cls((current.value -1) % 4)

    @classmethod
    def right(cls, current):
        """Rotate the direction 90 degrees to the right (clockwise)."""
        return cls((current.value +1) % 4)

    def __str__(self):
        return self.name



