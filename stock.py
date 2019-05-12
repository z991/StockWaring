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
        return current_stock, current_price
