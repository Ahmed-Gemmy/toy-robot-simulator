from command.base import Command

class ReportCommand(Command):
    def execute(self, robot: "Robot") -> None:
        return robot.report()