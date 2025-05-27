import unittest
from command.move import MoveCommand
from command.place import PlaceCommand
from direction import Direction
from position import Position
from robot import Robot
from table import Table


class TestMoveCommand(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.robot = Robot(self.table)

    def test_move_forward_north(self):
        PlaceCommand(0, 0, Direction.NORTH).execute(self.robot)
        MoveCommand().execute(self.robot)

        self.assertEqual(self.robot.position, Position(0, 1))
        self.assertEqual(self.robot.direction, Direction.NORTH) # Same direction

    def test_move_ignored_if_fall(self):
        PlaceCommand(0, 4, Direction.NORTH).execute(self.robot)
        MoveCommand().execute(self.robot)

        self.assertEqual(self.robot.position, Position(0, 4)) # Same position
        self.assertEqual(self.robot.direction, Direction.NORTH)  # Same direction

    def test_move_ignored_if_not_placed(self):
        MoveCommand().execute(self.robot)
        self.assertEqual(self.robot.is_placed, False)

if __name__ == '__main__':
    unittest.main()