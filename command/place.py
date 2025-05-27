from command.base import Command

class PlaceCommand(Command):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def execute(self, robot):
        robot.place(self.x, self.y, self.direction)