import unittest
from command.place import PlaceCommand
from command.right import RightCommand
from direction import Direction
from robot import Robot
from table import Table


class RightCommandTest(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.robot = Robot(self.table)

    def test_turn_right_from_north(self):
        PlaceCommand(2, 2, Direction.NORTH).execute(self.robot)
        RightCommand().execute(self.robot)

        self.assertEqual(self.robot.direction, Direction.EAST)

    def test_ignored_if_not_placed(self):
        RightCommand().execute(self.robot)

        self.assertFalse(self.robot.is_placed)

if __name__ == '__main__':
    unittest.main()