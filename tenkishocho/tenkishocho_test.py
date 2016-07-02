#encoding: utf-8

import unittest

from tenkishocho import HourPerDayTenki

class HourPerDayTenkiTest(unittest.TestCase):
    def setUp(self):
        self.hpdt = HourPerDayTenki(2016, 4, 1)

    def test_get_temparature(self):
        """
        test get_temparature() method
        """
        one_day_temparature_dict = self.hpdt.get_temparature()
        self.assertEqual(one_day_temparature_dict[1], 13.3)
        self.assertEqual(one_day_temparature_dict[5], 11.2)
        self.assertEqual(one_day_temparature_dict[10], 16.7)

if __name__ == "__main__":
    unittest.main()
