# tenkishocho

Get weather information in Japan from KISHOCHO WEB SYSTEM.

## Test
```
$ cd tenkishocho
$ python -m unittest tenkisho_test.py
```

## Usage

CAUTION!
Python2 does not work on this library

All APIs can be available like this

```
from tenkishocho import HourPerDayTenki
```

### Example Usage

#### HourPerDayTenki
```
>>> tenki = HourPerDayTenki(2016, 4, 1) # Default Location is Tokyo/Tokyo
>>> tenki.get_temparature() # Get Temparature data per an hour
{1: 13.3, 2: 13.8, 3: 13.0, 4: 12.2, 5: 11.2, 6: 10.8, 7: 12.1, 8: 13.8, 9: 15.3, 10: 16.7, 11: 16.9, 12: 17.2, 13: 17.0, 14: 15.7, 15: 14.3, 16: 13.0, 17: 12.2, 18: 11.4, 19: 11.1, 20: 10.9, 21: 9.5, 22: 8.5, 23: 8.2, 24: 8.4}
```

#### DayPerMonthTenki
```
>>> dpmt = DayPerMonthTenki(2016, 4) # Default Location is Tokyo/Tokyo
>>> dmpt.get_max_temperature()[1]  # Max Temparature of 1st, April
18.4
```
