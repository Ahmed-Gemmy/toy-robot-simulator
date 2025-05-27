from command.factory import CommandFactory
from robot import Robot
from table import Table


class Simulator:
    def __init__(self):
        self.table = Table()
        self.robot = Robot(self.table)
        self.last_report = None

    def execute(self, line:str):
        command = CommandFactory.create(line)
        if command is None:
            return None

        result = command.execute(self.robot)

        if isinstance(result, str): # Only report command can return string
            self.last_report = result
            return result
        return None
