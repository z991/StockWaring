import time
from handleconfig import ConfigStock
from dingding import Ding
from stock import Stock
from condition import Condition


def send_waring(stock_name):
    """
    发送报警信息
    :param config文件中股票的配置名称:
    :return:
    """
    config = ConfigStock()
    message = config.config_message(stock_name)
    hight, low, stock_num = message
    stock = Stock(stock_num)
    current_stock, current_price = stock.get_current()

    if '股票代码错误' in current_stock:
        message = '股票 {} ,请输入正确股票代码！'.format(current_stock)
    elif current_price > hight:
        message = '股票 {} ,现价为{},大于卖出阀值{},可以卖出'.format(current_stock, current_price, hight)
    elif current_price < low:
        message = '股票 {} ,现价为{},小于买入阀值{},可以买入'.format(current_stock, current_price, low)
    return message

if __name__ == '__main__':
    ding = Ding()
    while True:
        condition = Condition()
        stock_deal = condition.stock_deal()
        if stock_deal == 1:
            message = send_waring('stock')
            ding.send(message)
