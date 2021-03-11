"""Не работает"""

from Selenium_parse import fly_selenium
import time


class hotel_selenium(fly_selenium):

    def click(self, price_min, price_max):
        price_but = self.browser.find_element_by_class_name("_t6p96s")
        price_but.click()
        time.sleep(1000)


class Hotel_parser:

    def __init__(self, city, date_start, date_finish, price):
        self.city = city
        self.date_start = date_start
        self.date_finish = date_finish
        self.price = price
        a = hotel_selenium("https://www.airbnb.ru/s/Moscow--%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F/homes?tab_id"
                           "=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april"
                           "&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip"
                           "&date_picker_type=calendar&checkin=2021-03-06&checkout=2021-04-16&adults=1&query=Moscow"
                           "%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F&place_id=ChIJybDUc_xKtUYRTM9XV8zWRD0&source"
                           "=structured_search_input_header&search_type=autocomplete_click")
        a.click(1, 1)

    def __link_update(self):
        pass

    def __get(self):
        pass


b = Hotel_parser("Москва", 1, 1, 1)
