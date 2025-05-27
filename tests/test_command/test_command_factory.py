import unittest

from command.factory import CommandFactory
from command.left import LeftCommand
from command.move import MoveCommand
from command.place import PlaceCommand
from command.report import ReportCommand
from command.right import RightCommand
from direction import Direction


class TestCommandFactory(unittest.TestCase):
    def test_parse_place_command(self):
        cmd = CommandFactory.create("PLACE 1,2,NORTH")
        self.assertIsInstance(cmd, PlaceCommand)
        self.assertEqual(cmd.x, 1)
        self.assertEqual(cmd.y, 2)
        self.assertEqual(cmd.direction, Direction.NORTH)

    def test_parse_move_command(self):
        cmd = CommandFactory.create("MOVE")
        self.assertIsInstance(cmd, MoveCommand)

    def test_parse_left_command(self):
        cmd = CommandFactory.create("LEFT")
        self.assertIsInstance(cmd, LeftCommand)

    def test_parse_right_command(self):
        cmd = CommandFactory.create("RIGHT")
        self.assertIsInstance(cmd, RightCommand)

    def test_parse_report_command(self):
        cmd = CommandFactory.create("REPORT")
        self.assertIsInstance(cmd, ReportCommand)

    def test_invalid_command(self):
        self.assertIsNone(CommandFactory.create("INVALID"))
        self.assertIsNone(CommandFactory.create("PLACE 5,5,UP"))
        self.assertIsNone(CommandFactory.create("PLACE X,Y,NORTH"))
        self.assertIsNone(CommandFactory.create(""))
        self.assertIsNone(CommandFactory.create("PLACE"))
        self.assertIsNone(CommandFactory.create("PLACE 1,2"))
        self.assertIsNone(CommandFactory.create("PLACE 1,SOUTH"))
        self.assertIsNone(CommandFactory.create("REPORT NOW"))
        self.assertIsNone(CommandFactory.create("MOVE ROBOT"))
        self.assertIsNone(CommandFactory.create("RIGHT ROBOT"))
        self.assertIsNone(CommandFactory.create("LEFT ROBOT"))

if __name__ == '__main__':
    unittest.main()
