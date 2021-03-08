import requests
import json
class hotel_api:
    def __init__(self, city, start_date, finish_date):
        self.city=city
        self.start_date = start_date
        self.finish_date = finish_date

    def __linkup(self):
        link_city = "location=" + self.city
        link_currency = "&currency=rub"
        link_start_date ="&checkIn=" + self.start_date
        link_finish_date = "&checkOut=" + self.finish_date
        link_limit = "&limit=100"
        self.link = "http://engine.hotellook.com/api/v2/cache.json?"+link_city+link_currency+link_start_date+link_finish_date+link_limit

    def __getData(self):
        self.__linkup()
        data = requests.get(self.link)
        return data

    def __getInfo(self):
        data = __getData()

a = hotel_api("Moscow", "2021-12-10", "2021-12-12")
