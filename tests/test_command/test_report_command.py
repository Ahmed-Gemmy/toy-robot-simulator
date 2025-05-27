import unittest

from command.place import PlaceCommand
from command.report import ReportCommand
from robot import Robot
from table import Table
from direction import Direction


class TestReportCommand(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.robot = Robot(self.table)

    def test_report_after_place(self):
        PlaceCommand(1, 2, Direction.WEST).execute(self.robot)
        output = ReportCommand().execute(self.robot)
        self.assertEqual(output, "1,2,WEST")

    def test_report_ignored_if_not_placed(self):
        output = ReportCommand().execute(self.robot)
        self.assertIsNone(output)

if __name__ == '__main__':
    unittest.main()
