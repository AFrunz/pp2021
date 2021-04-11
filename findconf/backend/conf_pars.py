"""Парсер конференций. Требует доработки
Входные данные: Страна проживания, город проживания, тема конференции, диапазон удобных дат, ключевые слова.
Выходные данные: Словарь значений(Название, дата начала, дата конца, дата конца подачи заявок, страна, город, ссылка
Доработать:
1) Поменять словарь, текущая реализация убога. Сделать обычный словарь (сделано)
2) Добавить фильтр дат прямо сюда, отсеивать конференции сразу, если дата не совпадает,
добавить проверку на дату конца подачи заявок, она должна быть больше текущей даты. (сделано)
3) Добавить модификатор ссылки

"""

import requests
from bs4 import BeautifulSoup as BS
from findconf.backend.hotel_api import strtodate

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.111 Safari/537.36', 'accept': '*/*',
           'cookie': 'G_AUTHUSER_H=0; G_ENABLED_IDPS=google; _ga=GA1.1.1708452945.1603900516; G_AUTHUSER_H=0; df_id=93a48948b52daf05e4f48c9f0e15a37d; xf_user=3626977%2C5095f49fae7649341ebe39a668dc4d66fc2cf4a6; xf_logged_in=1; xf_session=736654ce9b5a156fdf2bf94a69c0265b; xf_market_items_viewed=8103659; xf_market_custom_cat_id=2; xf_market_search_url=%2Fmarket%3Fcategory_id%3D2%26_loadSearchBar%3Dtrue%26title%3D%26_xfRequestUri%3D%252Fmarket%252F%26_xfNoRedirect%3D1%26_xfToken%3D3626977%252C1604229396%252C385cb84b3d3bb290650e7a0e188a6514f1eafb89%26_xfResponseType%3Djson; _ga_J7RS527GFK=GS1.1.1604227707.6.1.1604229406.0'
           }


class Conf_parser:
    """Общий класс для парсинга конференций"""
    link = 'https://konferencii.ru/search?advance%5Bkeyword%5D=&advance%5BsearchOr%5D=1&advance%5BstartDate%5D=&advance_startDate=&advance%5BendDate%5D=&advance_endDate=&advance%5Bbackup%5D=1&advance%5BlastRequestDate1%5D=&advance_lastRequestDate1=&advance%5BlastRequestDate2%5D=&advance_lastRequestDate2=&advance%5BcountryId%5D=&advance%5BcityId%5D=&advance%5BeventId%5D=&advance%5BtopicId%5D%5B%5D=40&advance%5BparticalId%5D=&advance%5BorderBy%5D=startDate&advance%5Blimit%5D=20&submit=%D0%98%D1%81%D0%BA%D0%B0%D1%82%D1%8C'

    def __init__(self, date1, date2, keywords, theme):
        self.theme = theme
        self.date1 = date1
        self.date2 = date2
        self.keywords = keywords
        self.__linkUpdate()
        self.__parse()

    def getRes(self):
        """Получение результатов парсинга"""
        return self.result

    def __linkUpdate(self):
        """Модификация ссылки с учетом вводных данных"""
        keywords = ''
        if self.keywords is None:
            self.keywords = ''
        if self.theme is None:
            self.theme = ''
        url_f = "https://konferencii.ru/search?advance%5Bkeyword%5D="
        url_s = "&advance%5BsearchOr%5D=1&advance%5BstartDate%5D=&advance_startDate=&advance%5BendDate%5D=&advance_endDate=&advance%5Bbackup%5D=1&advance%5BlastRequestDate1%5D=&advance_lastRequestDate1=&advance%5BlastRequestDate2%5D=&advance_lastRequestDate2=&advance%5BcountryId%5D=&advance%5BcityId%5D=&advance%5BeventId%5D=&advance%5BtopicId%5D%5B%5D="
        url_t = "&advance%5BparticalId%5D=&advance%5BorderBy%5D=startDate&advance%5Blimit%5D=10&submit=Искать"
        znaki = [",", ";", "!", "?", ":"]
        for i in znaki:
            keywords = self.keywords.replace(i, " ")
        keywords = keywords.replace(" ", "+")
        url = url_f + keywords + url_s + self.theme + url_t
        self.link = url

    def __parse(self):
        """Основа парсера"""
        Html = self.__getHTML()
        self.result = self.__getInf(Html)

    def __getHTML(self):
        """Получение HTML кода"""
        link = self.link
        return requests.get(link, headers=HEADERS)

    def __check(self, start, finish):
        """Проверка на дату"""
        if self.date2 == -1 and self.date1 == -1:
            return True
        elif self.date1 == -1:
            return self.date2 >= strtodate(start) and self.date2 >= strtodate(finish)
        if self.date2 >= strtodate(start) >= self.date1 and self.date2 >= \
                strtodate(finish) >= self.date1:
            return True
        return False

    def __getInf(self, html):
        """Получение необходимой информации"""
        new_html = BS(html.text, "html.parser")
        array_of_inf = []
        All_element = new_html.find_all("div", class_="row1 index_cat_1st")
        All_element = All_element + new_html.find_all("div", class_="row2 index_cat_1st")
        link_base = "https://konferencii.ru/"
        for i in All_element:
            at = {"Name": None,
                  "date_start": None,
                  "date_end": None,
                  "application_end": None,
                  "Country": None,
                  "city": None,
                  "link": None,
                  "code": None,
                  "train": None,
                  "plane": None,
                  "hotel": None}
            i = i.find("div", class_="index_cat_txt")
            # Достаем различные даты
            s = i.find("div", class_="left").get_text()
            s = s.replace(" ", "")
            s = s[s.find('\n') + 1:]
            # Дата начала
            at["date_start"] = s[:s.find('.')]
            s = s[s.find('\n') + 1:]
            # Дата конца
            at["date_end"] = s[:s.find('.')]
            s = s[s.find('\n') + 1:]
            s = s[s.find('\n') + 1:]
            # Дата конца регистрации
            at["application_end"] = s[:s.find('.')]
            # Проверка на дату
            if not self.__check(at["date_start"], at["date_end"]):
                continue
            # Выгружаем ссылку и название
            s = str(i.find("div", class_="index_cat_tit").find("a"))
            s = s[s.find("=\"") + 2:]
            at["link"] = link_base + s[:s.find("\"")]
            at["Name"] = s[s.find(">") + 1:s.find("<")]
            # Выгружаем город и страну
            s = str(i.find("div", class_="left").find_next("div", class_="left").find("p", class_="ross_p").find("b"))
            at["Country"] = s[s.find(">") + 1:s.find(",")]
            at["city"] = s[s.find(",") + 2:s.rfind("<")]
            array_of_inf.append(at)
        return array_of_inf


# a = Conf_parser(1, 1, "31марта2021г", "31июня2022г", 1, 1)
# print(a.getRes())
