import datetime

import requests


class Stock:

    def __init__(self, stock_num):
        self.stock_num = stock_num

    def get_current(self):
        """
        获取实时股票信息
        :return:
        """
        url = "http://hq.sinajs.cn/list={}".format(self.stock_num)
        stock_info = requests.get(url).text
        try:
            current_price = stock_info.split(',')[3]
            current_stock = stock_info.split(',')[0].split('="')[-1]
        except Exception as e:
            current_price = '0'
            current_stock = '股票代码错误' + str(e)
        current_price = float(current_price)
        return current_stock, current_price

    def get_rec_60(self):
        yes_date = datetime.datetime.now() - datetime.timedelta(days=1)
        before_60 = yes_date - datetime.timedelta(days=59)
        now_data_str = datetime.datetime.strftime(yes_date, "%Y%m%d")
        before_60_str = datetime.datetime.strftime(before_60, "%Y%m%d")
        url = f"https://q.stock.sohu.com/hisHq?code=cn_{self.stock_num[2:]}&start={before_60_str}&end={now_data_str}"
        res = requests.get(url=url)
        return res.json()
