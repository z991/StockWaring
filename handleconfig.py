import configparser


class ConfigStock:
    """
    获取股票配置信息
    """
    conf = configparser.ConfigParser()

    def __init__(self):
        self.conf_main = configparser.ConfigParser()
        self.conf = self.conf_main.read("config.ini")

    def dingding_config(self, dingding):
        webhook = self.conf_main.get(dingding, 'webhook')
        return webhook

    def config_message(self, stock):
        hight = self.conf_main.get(stock, 'high')
        low = self.conf_main.get(stock, 'low')
        stock_num = self.conf_main.get(stock, 'stock_num')
        return hight, low, stock_num
