import requests
from dingtalkchatbot.chatbot import DingtalkChatbot
import configparser
import datetime
import time

conf = configparser.ConfigParser()


class Ding:

    def __init__(self):
        self.webhook = 'https://oapi.dingtalk.com/robot/send?access_token=6e2ce71ae16374dd4edbdf6d1b12a605599e34da3e1ce92c98199def3eadcea2'

    def send(self, message):
        xiaoding = DingtalkChatbot(self.webhook)
        xiaoding.send_text(msg=message, is_at_all=True)


class Stock:

    def __init__(self, stock_num):
        self.stock_num = stock_num

    def get_current(self):
        """
        获取股票信息
        :return:
        """
        url = "http://hq.sinajs.cn/list={}".format(self.stock_num)
        stock_info = requests.get(url).text
        print('stock_info===', stock_info)
        try:
            current_price = stock_info.split(',')[3]
            current_stock = stock_info.split(',')[0].split('="')[-1]
        except Exception as e:
            current_price = '0'
            current_stock = '股票代码错误' + str(e)
        return current_stock, current_price


class Warning:

    def __init__(self):
        self.conf = conf.read("config.ini")
        self.hight = conf.get('stock', 'high')
        self.low = conf.get('stock', 'low')
        self.stock_num = conf.get('stock', 'stock_num')

    def condion(self):
        """
        判断是否为股票交易时间
        :return:
        """
        now = datetime.datetime.now()
        hour = now.hour
        min = now.minute
        week = now.weekday()

        result = 1

        if (week not in range(1, 6)) or ((hour == 9 or hour == 11) and min in (0, 31)) or (
                hour in range(0, 9) or hour in range(15, 24)):
            result = 0

        return result

    def sen_waring(self):
        """
        发送提醒信息
        :return:
        """
        stock = Stock(self.stock_num)
        current_stock, current_price = stock.get_current()
        ding = Ding()

        if '股票代码错误' in current_stock:
            ding.send(message='股票 {} ,请输入正确股票代码！'.format(current_stock))

        elif current_price > self.hight:
            ding.send(message='股票 {} ,现价为{},大于卖出阀值{},可以卖出'.format(current_stock, current_price, self.hight))

        elif current_price < self.low:
            ding.send(message='股票 {} ,现价为{},小于买入阀值{},可以买入'.format(current_stock, current_price, self.low))


if __name__ == '__main__':
    while True:
        waring = Warning()
        if waring.condion() == 1:
            time.sleep(2)
            waring.sen_waring()
        else:
            continue
