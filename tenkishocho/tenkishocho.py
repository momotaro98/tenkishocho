#!/bin/env python
# condig: utf-8
import urllib.request
from html.parser import HTMLParser

URLBASE='http://www.data.jma.go.jp/obd/stats/etrn/view/'

def return_the_page_from_url(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    the_page = response.read() # response.read()はstr型っぽい
    the_page = the_page.decode('utf-8') # この代入前のthe_pageはバイト列型っぽい
    return the_page


class TenkishochoHTMLParser(HTMLParser):
    """
    気象庁ホームページのデータHTMLにとって汎用的なHTMLParserクラス
    HTMLにおける天気データのテーブル部分のみを保持する
    基準となるtrタグを見つけたら、その中のtdを取得する

    テストを書いた方が良さそう

    ISUE: 表における空のものはself.tableに入らないので、受け取った側で補填を任せている状態
    """
    def __init__(self, *set_attr_pairs):
        super().__init__() # HTMLParserから継承する
        self.set_attr_set = { _p for _p in set_attr_pairs }
        self.table = [] # 外から見せる
        self._rowlist = []
        self._rowflag = False

    def handle_starttag(self, tag, attrs):
        '''テストを書いた方が良さそう '''

        # 欲しいテーブルの条件から検証
        if tag == "tr":
            attr_set = { (_a[0], _a[1]) for _a in attrs }
            if attr_set == self.set_attr_set:
                self._rowflag = True

    def handle_endtag(self, tag):
        if self._rowflag and tag == "tr":
            self.table.append(tuple(self._rowlist))
            self._rowflag = False
            self._rowlist = []

    def handle_data(self, data):
        if self._rowflag == True:
            self._rowlist.append(data)


class HourPerDayTenki(object):
    """
    description comming soon...
    """

    def __init__(self, year, month, day ,prec_no=44, block_no=47662):
        """ default region: Tokyo(prec_no=44), Tokyo(block_no=47662) """
        self.year = year
        self.month = month
        self.day = day
        self.prec_no = prec_no
        self.block_no = block_no

        self._url = URLBASE + 'hourly_s1.php?' +\
            'prec_no={0}&'.format(prec_no) +\
            'block_no={0}&'.format(block_no) +\
            'year={0}&'.format(year) +\
            'month={0}&'.format(month) +\
            'day={0}&'.format(day) +\
            'view='

        self._page = return_the_page_from_url(self._url)
        self._parser = TenkishochoHTMLParser(('class', 'mtx'), ('style', 'text-align:right;'))
        self._parser.feed(self._page) # self._parserにはテーブルデータがある

        '''ここにself._parser.tableの分析(空文字対処用)のプログラムを加える必要あり'''

        self._table = tuple(self._parser.table) # self._parserにはテーブルデータがある

        '''
        self._parser.tableは全部で
        (時、現地気圧、海面気圧、降水量、気温、露天温度、蒸気圧、湿度、風速、風向、日照時間、全天日射量、降雪、積雪、天気、雲量、視程)
        self._table -> (
                            ('1', '1005.6', '1008.4', '--', '18.6', '16.2', ...),
                            ('2', '1006.5', '1009.4', '--', '17.6', '12.2', ...),
                            .
                            .
                            .
                        )
        '''

    def get_kind_dict(self):
        """
        get all data in weather kind dict structure

        Example returned dictionary
        dict -> {
            'temparature': {1: 19.3, 2: 19.6, ...},
            'humidity': {1: 65.3, 2: 67.6, ...},
            ...
        }
        """
        pass

    def get_temparature(self):
        """
        get all data in weather kind dict structure

        Example returned dictionary
            {1: 19.3,
             2: 19.6,
             3: 20.8,
             .
             .
             .
             }
        """
        return {int(row[0]): float(row[4]) for row in self._table} # 5番目のカラムは気温



class DayPerMonthTenki(object):
    """
    description comming soon...
    """

    def __init__(self, year, month, prec_no=44, block_no=47662):
        """ default region: Tokyo(prec_no=44), Tokyo(block_no=47662) """
        self.year = year
        self.month = month
        self.prec_no = prec_no
        self.block_no = block_no

        self._url = URLBASE + 'daily_s1.php?' +\
            'prec_no={0}&'.format(prec_no) +\
            'block_no={0}&'.format(block_no) +\
            'year={0}&'.format(year) +\
            'month={0}'.format(month)

        self._page = return_the_page_from_url(self._url)
        self._parser = TenkishochoHTMLParser(('class', 'mtx'), ('style', 'text-align:right;'))
        self._parser.feed(self._page) # self._parserにはテーブルデータがある

        '''ここにself._parser.tableの分析(空文字対処用)のプログラムを加える必要あり'''

        self._table = tuple(self._parser.table) # self._parserにはテーブルデータがある

        '''
        月日ごとページにおいて
        self._parser.tableは全部で
        (日、現地気圧(平均)、海面気圧(平均)、降水量(合計)、降水量(1時間最大)、降水量(10分間最大)、気温(平均)、気温(最高)、気温(最低)、湿度(平均)、湿度(最小)、平均風速、最大風速、最大風速風向、最大瞬間風速風速、最大瞬間風速風向、日照時間、積雪合計、最深積雪値、天気情報(昼)、天気情報(夜))
        self._table -> (
                        ('1', '1005.6', '1008.4', '--', '--', '--', ...),
                        ('2', '1006.5', '1009.4', '--', '--', '--', ...),
                        .
                        .
                        .
                        )
        '''

    def get_kind_dict(self):
        """
        get all data in weather kind dict structure

        Example returned dictionary
        dict -> {
            'temparature': {1: 19.3, 2: 19.6, ...},
            'humidity': {1: 65.3, 2: 67.6, ...},
            ...
        }
        """
        pass

    def get_ave_temparature(self):
        """
        get all data in weather kind dict structure

        Example returned dictionary
            {1: 19.3,
             2: 19.6,
             3: 20.8,
             .
             .
             .
             31: 20.1}
        """
        return {int(row[0]): float(row[6]) for row in self._table} # 7番目のカラムが気温
