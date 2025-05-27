import unittest
from robot import Robot
from table import Table
from direction import Direction
from command.place import PlaceCommand
from command.left import LeftCommand

class TestLeftCommand(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.robot = Robot(self.table)

    def test_turn_left_from_north(self):
        PlaceCommand(2, 2, Direction.NORTH).execute(self.robot)
        LeftCommand().execute(self.robot)
        self.assertEqual(self.robot.direction, Direction.WEST)

    def test_ignored_if_not_placed(self):
        LeftCommand().execute(self.robot)
        self.assertFalse(self.robot.is_placed)

if __name__ == "__main__":
    unittest.main()
