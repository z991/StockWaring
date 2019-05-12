import datetime


class Condition:

    def stock_deal(self):
        """
        判断是否为股票交易日
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
