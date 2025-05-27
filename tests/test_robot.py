import unittest

from position import Position
from robot import Robot
from table import Table
from direction import Direction

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.table = Table(5,5)
        self.robot = Robot(self.table)

    def test_initial_state_not_placed(self):
        self.assertFalse(self.robot.is_placed)

    def test_valid_place(self):
        self.robot.place(1,2, Direction.NORTH)

        self.assertTrue(self.robot.is_placed)
        self.assertEqual(self.robot.position, Position(1,2))
        self.assertEqual(self.robot.direction, Direction.NORTH)

    def test_invalid_place(self):
        self.robot.place(5,5, Direction.NORTH)
        self.assertFalse(self.robot.is_placed) # Place ignored

    def test_move_within_bounds(self):
        self.robot.place(0, 0, Direction.NORTH)
        self.robot.move()
        self.assertEqual(self.robot.position, Position(0,1)) # Moved one step north
        self.assertEqual(self.robot.direction, Direction.NORTH) # Same direction

    def test_move_off_table_ignored(self):
        self.robot.place(0, 4, Direction.NORTH)
        self.robot.move()
        self.assertEqual(self.robot.position, Position(0,4)) # No change
        self.assertEqual(self.robot.direction, Direction.NORTH) # Same direction

    def test_turn_left(self):
        self.robot.place(1,1, Direction.NORTH)
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, Direction.WEST) # facing west
        self.assertEqual(self.robot.position, Position(1,1)) # Same position

    def test_turn_right(self):
        self.robot.place(1,1, Direction.NORTH)
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, Direction.EAST) # facing east
        self.assertEqual(self.robot.position, Position(1,1)) # Same position

    def test_report(self):
        self.robot.place(3, 3, Direction.SOUTH)
        self.assertEqual(self.robot.report(), "3,3,SOUTH")

if __name__ == '__main__':
    unittest.main()