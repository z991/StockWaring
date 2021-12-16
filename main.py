from handleconfig import ConfigStock
from dingding import Ding
from stock import Stock
from trading import Trading


def send_waring(stock_num, high, low):
    """
    发送报警信息
    :param config文件中股票的配置名称:
    :return:
    """
    high = float(high)
    low = float(low)
    stock = Stock(stock_num)
    current_stock, current_price = stock.get_current()
    message = None
    if '股票代码错误' in current_stock:
        message = '股票 {} ,请输入正确股票代码！'.format(current_stock)
    elif current_price > high:
        message = '股票 {} ,现价为{},大于卖出阀值{},可以卖出'.format(current_stock, current_price, high)
    elif current_price < low:
        message = '股票 {} ,现价为{},小于买入阀值{},可以买入'.format(current_stock, current_price, low)
    return message


if __name__ == '__main__':
    while True:
        config = ConfigStock()
        ding = Ding()
        condition = Trading()
        task_status = condition.is_start(config)

        if task_status == 1:
            stock_list = config.get_stock_json()
            for stock in stock_list:
                stock_num = stock['stock_num']
                high = stock['high']
                low = stock['low']
                stop = stock['stop']

                if str(stop) == '1':
                    continue
                message = send_waring(stock_num, high, low)
                if message:
                    ding.send(message)
