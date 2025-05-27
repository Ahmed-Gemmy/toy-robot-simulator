from command.left import LeftCommand
from command.move import MoveCommand
from command.place import PlaceCommand
from command.report import ReportCommand
from command.right import RightCommand
from direction import Direction


class CommandFactory:
    @staticmethod
    def create(input_str: str):

        parts = input_str.strip().split()
        if not parts:
            return None

        cmd = parts[0].upper()

        if cmd == "PLACE":
            if len(parts) != 2:
                return None
            try:
                x_str, y_str, dir_str = parts[1].split(",")
                x, y = int(x_str), int(y_str)
                direction = Direction[dir_str.upper()]
                return PlaceCommand(x, y, direction)
            except (ValueError, KeyError):
                return None

        elif cmd == "MOVE" and len(parts) == 1:
            return MoveCommand()
        elif cmd == "RIGHT" and len(parts) == 1:
            return RightCommand()
        elif cmd == "LEFT" and len(parts) == 1:
            return LeftCommand()
        elif cmd == "REPORT" and len(parts) == 1:
            return ReportCommand()

        return None
