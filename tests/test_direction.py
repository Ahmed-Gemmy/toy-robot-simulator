import unittest

from direction import Direction

class TestDirection(unittest.TestCase):
    def test_left_turn(self):
        self.assertEqual(Direction.left(Direction.NORTH), Direction.WEST)
        self.assertEqual(Direction.left(Direction.WEST), Direction.SOUTH)
        self.assertEqual(Direction.left(Direction.SOUTH), Direction.EAST)
        self.assertEqual(Direction.left(Direction.EAST), Direction.NORTH)

    def test_right_turn(self):
        self.assertEqual(Direction.right(Direction.NORTH), Direction.EAST)
        self.assertEqual(Direction.right(Direction.EAST), Direction.SOUTH)
        self.assertEqual(Direction.right(Direction.SOUTH), Direction.WEST)
        self.assertEqual(Direction.right(Direction.WEST), Direction.NORTH)

if __name__ == '__main__':
    unittest.main()