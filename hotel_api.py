"""получение данных цен на отели (сделано)"""
"""Нужно преобразовать дату"""
"""Сделал"""

import requests
import json


def strtodate(date):
    day = ''
    month = ''
    d = {"янв": "01", "фев": "02", "мар": "03", "апр": "04", "ма": "05", "июн": "06",
         "июл": "07", "ав": "08", "сен": "09", "окт": "10", "ноя": "11", "дек": "12"}
    for j in d:
        pos = date.find(j)
        if pos != -1:
            if pos == 1:
                day = '0' + date[:pos]
            else:
                day = date[:pos]
            month = d[j]
            break
    if day != '':
        new_date = date[-5:-1] + '-' + month + '-' + day
        return new_date
    return date


class hotel_api:

    def __init__(self, city, start_date, finish_date):
        self.city = city
        self.start_date = strtodate(start_date)
        self.finish_date = strtodate(finish_date)
        self.__getInfo()

    def __linkup(self):
        link_city = "location=" + self.city
        link_currency = "&currency=rub"
        link_start_date = "&checkIn=" + self.start_date
        link_finish_date = "&checkOut=" + self.finish_date
        link_limit = "&limit=1000"
        self.link = "http://engine.hotellook.com/api/v2/cache.json?" + link_city + link_currency + link_start_date + \
                    link_finish_date + link_limit

    def __getData(self):
        self.__linkup()
        data = requests.get(self.link)
        return data.text

    def __getInfo(self):
        data = self.__getData()
        info = json.loads(data)
        prices = []
        for i in range(0, len(info)):
            prices.append(info[i]["priceAvg"])
        prices = sorted(prices)
        if len(prices) > 0:
            sr = len(prices) // 2
            res = prices[sr]
            self.res = res
        else:
            self.res = -1

    def get_res(self):
        return self.res

