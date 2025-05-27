from command.base import Command

class MoveCommand(Command):
    def execute(self, robot: "Robot") -> None:
        robot.move()