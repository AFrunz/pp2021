"""получение данных цен на отели"""

import requests
import json


class hotel_api:

    def __init__(self, city, start_date, finish_date):
        self.city = city
        self.start_date = start_date
        self.finish_date = finish_date
        self.__getInfo()

    def __linkup(self):
        link_city = "location=" + self.city
        link_currency = "&currency=rub"
        link_start_date ="&checkIn=" + self.start_date
        link_finish_date = "&checkOut=" + self.finish_date
        link_limit = "&limit=1000"
        self.link = "http://engine.hotellook.com/api/v2/cache.json?"+ link_city+link_currency+link_start_date+link_finish_date+link_limit

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
        sr = len(prices) // 2
        print(prices[sr])
        return info


a = hotel_api("OGZ", "2021-12-10", "2021-12-12")