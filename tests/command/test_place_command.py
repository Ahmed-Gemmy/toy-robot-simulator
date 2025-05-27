import unittest

from command.place import PlaceCommand
from position import Position
from robot import Robot
from table import Table
from direction import Direction


class TestPlaceCommand(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.robot = Robot()

    def test_valid_place(self):
        cmd = PlaceCommand(2, 3, Direction.NORTH)
        cmd.execute(self.robot)

        self.assertTrue(self.robot.is_placed)
        self.assertEqual(self.robot.direction, Direction.NORTH)
        self.assertEqual(self.robot.position, Position(2,3))

    def test_invalid_place_out_of_bounds(self):
        cmd = PlaceCommand(5, 5, Direction.NORTH)

        cmd.execute(self.robot)

        self.assertFalse(self.robot.is_placed)

if __name__ == '__main__':
    unittest.main()