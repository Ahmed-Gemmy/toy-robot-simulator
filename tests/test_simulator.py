import unittest

from simulator import Simulator

class SimulatorTest(unittest.TestCase):
    def setUp(self):
        self.sim = Simulator()

    def test_ignore_commands_before_place(self):
        self.sim.execute("MOVE")
        self.sim.execute("REPORT")

        # Robot not yet placed.
        self.assertIsNone(self.sim.last_report)

    def test_simple_move(self):
        self.sim.execute("PLACE 0,0,NORTH")
        self.sim.execute("MOVE")
        self.sim.execute("REPORT")

        self.assertEqual(self.sim.last_report, "0,1,NORTH")

    def test_simple_rotation(self):
        self.sim.execute("PLACE 0,0,NORTH")
        self.sim.execute("RIGHT")
        self.sim.execute("REPORT")

        self.assertEqual(self.sim.last_report, "0,0,EAST")

        # Rotating back
        self.sim.execute("RIGHT")
        self.sim.execute("REPORT")
        self.assertEqual(self.sim.last_report, "0,0,NORTH")

    def test_simple_replace(self):
        self.sim.execute("PLACE 0,0,NORTH")
        self.sim.execute("REPORT")

        self.assertEqual(self.sim.last_report, "0,0,NORTH")

        # Placing in another location
        self.sim.execute("PLACE 2,2,WEST")
        self.sim.execute("REPORT")

        self.assertEqual(self.sim.last_report, "2,2,WEST")

    def test_rotation_and_move(self):
        self.sim.execute("PLACE 1,2,EAST")
        self.sim.execute("MOVE")
        self.sim.execute("MOVE")
        self.sim.execute("LEFT")
        self.sim.execute("MOVE")
        self.sim.execute("REPORT")
        self.assertEqual(self.sim.last_report, "3,3,NORTH")

    def test_invalid_place_is_ignored(self):
        self.sim.execute("PLACE 5,5,NORTH")
        self.sim.execute("MOVE")
        self.sim.execute("REPORT")
        self.assertIsNone(self.sim.last_report)

if __name__ == '__main__':
    unittest.main()




