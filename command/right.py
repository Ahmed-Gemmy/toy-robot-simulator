from command.base import Command

class RightCommand(Command):
    def execute(self, robot: "Robot") -> None:
        robot.turn_right()