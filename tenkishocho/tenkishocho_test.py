#encoding: utf-8

import unittest

from tenkishocho import HourPerDayTenki, DayPerMonthTenki

class HourPerDayTenkiTest(unittest.TestCase):
    def setUp(self):
        self.hpdt = HourPerDayTenki(2016, 4, 1)

    def test_get_temparature(self):
        """
        test get_temparature() method
        """
        tdict = self.hpdt.get_temparature()
        self.assertEqual(tdict[1], 13.3)
        self.assertEqual(tdict[5], 11.2)
        self.assertEqual(tdict[10], 16.7)


class DayPerMonthTenkiTest(unittest.TestCase):
    def setUp(self):
        # 2016年4月のデータを使用
        self.dpmt = DayPerMonthTenki(2016, 4)

    def test_get_ave_temperature(self):
        tdict = self.dpmt.get_ave_temperature()
        self.assertEqual(tdict[1], 12.8)
        self.assertEqual(tdict[2], 10.5)
        self.assertEqual(tdict[30], 16.0)

    def get_max_temperature(self):
        tdict = self.dpmt.get_max_temperature()
        self.assertEqual(tdict[1], 18.4)
        self.assertEqual(tdict[2], 13.3)
        self.assertEqual(tdict[30], 21.7)

    def test_get_day_tenki(self):
        tdict = self.dpmt.get_day_tenki()
        self.assertEqual(tdict[1], '曇')
        self.assertEqual(tdict[2], '曇一時雨')
        self.assertEqual(tdict[30], '晴')


if __name__ == "__main__":
    unittest.main()
