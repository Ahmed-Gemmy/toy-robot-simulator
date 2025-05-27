import unittest
from position import Position

class TestPosition(unittest.TestCase):
    def test_create_position(self):
        p = Position(1,2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_equality(self):
        p1 = Position(0, 0)
        p2 = Position(0, 0)
        p3 = Position(1, 0)

        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

if __name__ == '__main__':
    unittest.main()