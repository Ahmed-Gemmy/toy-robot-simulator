import unittest
from simulator import Simulator

class TestEndToEnd(unittest.TestCase):
    def test_scenario_a(self):
        sim = Simulator()
        commands = [
            "PLACE 0,0,NORTH",
            "MOVE",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "0,1,NORTH")

    def test_scenario_b(self):
        sim = Simulator()
        commands = [
            "PLACE 0,0,NORTH",
            "LEFT",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "0,0,WEST")

    def test_scenario_c(self):
        sim = Simulator()
        commands = [
            "PLACE 1,2,EAST",
            "MOVE",
            "MOVE",
            "LEFT",
            "MOVE",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "3,3,NORTH")

    def test_ignores_until_valid_place(self):
        sim = Simulator()
        commands = [
            "MOVE",
            "RIGHT",
            "PLACE 1,1,NORTH",
            "MOVE",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "1,2,NORTH")

    def test_multiple_place_overrides_state(self):
        sim = Simulator()
        commands = [
            "PLACE 0,0,NORTH",
            "MOVE",
            "PLACE 4,4,EAST",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "4,4,EAST")

    def test_full_rotation_left_and_right(self):
        sim = Simulator()
        commands = [
            "PLACE 1,1,NORTH",
            "LEFT", "LEFT", "LEFT", "LEFT",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "1,1,NORTH")

        commands = [
            "RIGHT", "RIGHT", "RIGHT", "RIGHT",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "1,1,NORTH")

    def test_move_blocked_by_table_edge(self):
        sim = Simulator()
        commands = [
            "PLACE 0,0,SOUTH",
            "MOVE",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "0,0,SOUTH")

    def test_case_and_whitespace_tolerance(self):
        sim = Simulator()
        commands = [
            "   place 1,2,east  ",
            "MoVe",
            "  LeFt ",
            " move  ",
            "REPORT "
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "2,3,NORTH")

    def test_ignores_bad_commands(self):
        sim = Simulator()
        commands = [
            "PLACE X,Y,NORTH",
            "PLACE 1,1,NORTHEAST",
            "PLACE 1,1,NORTH",
            "MOVE",
            "SPIN",
            "REPORT"
        ]
        for cmd in commands:
            sim.execute(cmd)
        self.assertEqual(sim.last_report, "1,2,NORTH")

if __name__ == "__main__":
    unittest.main()
