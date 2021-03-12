"""Парсер поездов, возвращает номер, ссылку, город, дату и вокзал отправления и прибытия, а также
рейтинг и цену ( доделано )"""
"""Сейчас считает среднюю по каждой категории"""

import requests
from bs4 import BeautifulSoup as BS
from hotel_api import strtodate

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.111 Safari/537.36', 'accept': '*/*',
           'cookie': 'G_AUTHUSER_H=0; G_ENABLED_IDPS=google; _ga=GA1.1.1708452945.1603900516; G_AUTHUSER_H=0; df_id=93a48948b52daf05e4f48c9f0e15a37d; xf_user=3626977%2C5095f49fae7649341ebe39a668dc4d66fc2cf4a6; xf_logged_in=1; xf_session=736654ce9b5a156fdf2bf94a69c0265b; xf_market_items_viewed=8103659; xf_market_custom_cat_id=2; xf_market_search_url=%2Fmarket%3Fcategory_id%3D2%26_loadSearchBar%3Dtrue%26title%3D%26_xfRequestUri%3D%252Fmarket%252F%26_xfNoRedirect%3D1%26_xfToken%3D3626977%252C1604229396%252C385cb84b3d3bb290650e7a0e188a6514f1eafb89%26_xfResponseType%3Djson; _ga_J7RS527GFK=GS1.1.1604227707.6.1.1604229406.0'
           }


def transliteration2(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia|A|B|V|G|D|E|E|Zh|Z|I|I|K|L|M|N|O|P|R|S|T|U|F|Kh|Tc|Ch|Sh|Shch||Y||E|Iu|Ia'.split(
        '|')
    return text.translate({ord(k): v for k, v in zip(cyrillic, latin)})


def strtodate2(date):
    date = strtodate(date)
    date = date[-2:] + '.' + date[-5:-3] + '.' + date[:4]
    return date

class train_dict:
    """Информация о поезеде"""

    def __init__(self):
        self.number = None
        self.link = None
        self.city_iz = None
        self.vokzal_iz = None
        self.citi_v = None
        self.vokzal_v = None
        self.time_iz = None
        self.time_v = None
        self.rating = None
        self.price = {"Люкс": 0, "Купе-Сьют": 0, "Сидячий": 0, "Купе": 0, "СВ": 0, "Плацкарт": 0, "Базовый класс": 0,
                      "Эконом класс": 0,
                      "Экономический +": 0, "Вагон-бистро": 0, "Бизнес класс": 0,
                      "Первый класс": 0, "Купе-переговорная": 0}

    def dict_print(self):
        print(self.number, self.link, self.city_iz, self.vokzal_iz, self.time_iz, self.citi_v, self.vokzal_v,
              self.time_v, self.rating)
        print(self.price)


class train_parse:
    """Класс для парсинга поездов"""

    def __init__(self, city_from, city_to, date_start, date_finish):
        self.city_from = transliteration2(city_from)
        self.city_to = transliteration2(city_to)
        self.date_start = strtodate2(date_start)
        self.date_finish = strtodate2(date_finish)
        self.__parse()

    def get_Res(self):
        """Получение результатов парсинга"""
        return self.result

    def get_average(self):
        aver_sum = train_dict()
        aver_kol = train_dict()
        for t in self.result:
            for k in t.price:
                if k not in aver_sum.price:
                    aver_sum.price[k] = 0
                    aver_kol.price[k] = 0
                if t.price[k] != 0:
                    aver_sum.price[k] += float(t.price[k])
                    aver_kol.price[k] += 1
        for k in aver_sum.price:
            if aver_kol.price[k] != 0:
                aver_sum.price[k] = round(aver_sum.price[k] / aver_kol.price[k], 2)
        print(aver_sum.price)

    def __linkUpdate(self):
        """Модификация ссылки с учетом вводных данных"""
        link = "https://www.ufs-online.ru/kupit-zhd-bilety/"
        to = "moskva/sankt-peterburg?date=24.03.2021&returnDate=25.03.2021"
        dop = self.city_from + '/' + self.city_to + '?date=' + self.date_start + "&returnDate=" + self.date_finish
        self.link = link + dop

    def __parse(self):
        """Основа парсера"""
        self.__linkUpdate()
        Html = self.__getHTML()
        self.result = self.__getInf(Html)

    def __getHTML(self):
        """Получение HTML кода"""
        link = self.link
        return requests.get(link, headers=HEADERS)

    def __getInf(self, html):
        """Получение необходимой информации"""
        new_html = BS(html.text, "html.parser")
        all = new_html.find_all("div", class_="wg-train-container")
        all_data = []
        for i in all:
            l = train_dict()
            i = i.find("div", class_="wg-block__inner wg-block__inner_no-padding-top")
            # Вытаскиваем номер, тип, город отправления и прибытия, оценку
            a = i.find("div", class_="wg-train-info wg-train-info_full")
            # Номер, тип и оценка
            b = a.find("div", class_="wg-train-info__cup")
            c = b.find("div", class_="wg-train-info__col").find("div", class_="wg-train-info__direct").find(
                "div", class_="wg-train-info__train").find("div", class_="wg-train-info__num")
            d = c.find("a", target="_blank")
            l.link = d.get("href")
            s = str(d)
            l.number = s[s.find("_blank") + 8:s.rfind("<")]
            # Тип
            c = c.find("span", class_="wg-train-info__number-link")
            if c is None:
                l.type = ""
            else:
                c = str(c)
                c = c[c.find(">") + 1:]
                l.type = c[c.find(">") + 1:c.find("</")]
            # Оценка
            b = str(b.find("div", class_="wg-train-rating"))
            b = b[b.find("Value\">") + 7:]
            l.rating = b[:b.find("<")]
            # Города, время и вокзалы отправления и прибытия
            a = i.find("div", class_="wg-train-options__wrap")
            b = a.find("div", class_="wg-track-info__col")
            l.time_iz = b.find("span", class_="wg-track-info__time").get_text()
            l.city_iz = b.find("span", class_="wg-track-info__direction").get_text()
            l.vokzal_iz = b.find("span", class_="wg-track-info__station").get_text()
            b = a.find_all("div", class_="wg-track-info__col")[1]
            l.time_v = b.find("span", class_="wg-track-info__time").get_text()
            l.city_v = b.find("span", class_="wg-track-info__direction").get_text()
            l.vokzal_v = b.find("span", class_="wg-track-info__station").get_text()
            # Цены
            a = i.find("div", class_="wg-wagon-type")
            a = a.find_all("div", "wg-wagon-type__item")
            for i in a:
                key = str(i.find("div", class_="wg-wagon-type__title").get_text())
                l.price[key] = str(i.find("span", class_="wg-wagon-type__price-value").get_text())[:-6].replace(',',
                                                                                                                '.').replace(
                    ' ', '')
            all_data.append(l)
        return all_data


