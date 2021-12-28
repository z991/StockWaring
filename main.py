import time

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
    # 浮点数
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
    # 配置类实例化
    config = ConfigStock()
    # 钉钉类实例化
    ding = Ding()
    # 交易日判断类实例化
    condition = Trading()
    # 判断是否交易日，1为交易日
    task_status = condition.is_start(config)

    if task_status == 1:
        # 获取需要监控的股票列表信息（包括股票编码、买入阈值、卖出阈值）
        stock_list = config.get_stock_json()
        for stock in stock_list:
            # 获取某个股票的信息
            stock_num = stock['stock_num']
            high = stock['high']
            low = stock['low']
            # 判断是否为非监控股票
            stop = stock['stop']

            if str(stop) == '1':
                continue
            # 判断是否有买入或者卖出的消息提醒
            message = send_waring(stock_num, high, low)
            if message:
                # 如果有的话就发送钉钉消息
                ding.send_text(message)
                # time.sleep(2)

