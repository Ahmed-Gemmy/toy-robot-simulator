from command.base import Command

class LeftCommand(Command):
    def execute(self, robot: "Robot") -> None:
        robot.turn_left()