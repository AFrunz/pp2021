"""Парсер конференций. Требует доработки
Входные данные: Страна проживания, город проживания, тема конференции, диапазон удобных дат, ключевые слова.
Выходные данные: Словарь значений(Название, дата начала, дата конца, дата конца подачи заявок, страна, город, ссылка
Доработать:
1) Поменять словарь, текущая реализация убога. Сделать обычный словарь
2) Добавить фильтр дат прямо сюда, отсеивать конференции сразу, если дата не совпадает,
добавить проверку на дату конца подачи заявок, она должна быть больше текущей даты.
3) Добавить модификатор ссылки

"""


import requests
from bs4 import BeautifulSoup as BS


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.111 Safari/537.36', 'accept': '*/*', 'cookie': 'G_AUTHUSER_H=0; G_ENABLED_IDPS=google; _ga=GA1.1.1708452945.1603900516; G_AUTHUSER_H=0; df_id=93a48948b52daf05e4f48c9f0e15a37d; xf_user=3626977%2C5095f49fae7649341ebe39a668dc4d66fc2cf4a6; xf_logged_in=1; xf_session=736654ce9b5a156fdf2bf94a69c0265b; xf_market_items_viewed=8103659; xf_market_custom_cat_id=2; xf_market_search_url=%2Fmarket%3Fcategory_id%3D2%26_loadSearchBar%3Dtrue%26title%3D%26_xfRequestUri%3D%252Fmarket%252F%26_xfNoRedirect%3D1%26_xfToken%3D3626977%252C1604229396%252C385cb84b3d3bb290650e7a0e188a6514f1eafb89%26_xfResponseType%3Djson; _ga_J7RS527GFK=GS1.1.1604227707.6.1.1604229406.0'
           }


class Global_dict:
    """Класс для характеристик конференций"""
    def __init__(self):
        self.Name = None
        self.date_start = None
        self.date_end = None
        self.application_end = None
        self.Country = None
        self.city = None
        self.link = None
        self.code= None
        self.train = None
        self.plane = None
        self.hotel = None

    def Print_s(self):
        print(self.date_start, self.date_end, self.application_end, self.Name, self.link, self.city, self.Country, self.code, self.train, self.plane, self.hotel)


class Conf_parser:
    """Общий класс для парсинга конференций"""
    link = 'https://konferencii.ru/search?advance%5Bkeyword%5D=&advance%5BsearchOr%5D=1&advance%5BstartDate%5D=&advance_startDate=&advance%5BendDate%5D=&advance_endDate=&advance%5Bbackup%5D=1&advance%5BlastRequestDate1%5D=&advance_lastRequestDate1=&advance%5BlastRequestDate2%5D=&advance_lastRequestDate2=&advance%5BcountryId%5D=&advance%5BcityId%5D=&advance%5BeventId%5D=&advance%5BtopicId%5D%5B%5D=40&advance%5BparticalId%5D=&advance%5BorderBy%5D=startDate&advance%5Blimit%5D=20&submit=%D0%98%D1%81%D0%BA%D0%B0%D1%82%D1%8C'

    def __init__(self, country, city, date, theme):
        self.theme = theme
        self.date = date
        self.city = city
        self.country = country
        self.__parse()

    def getRes(self):
        """Получение результатов парсинга"""
        return self.result

    def __linkUpdate(self):
        """Модификация ссылки с учетом вводных данных"""
        pass

    def __parse(self):
        """Основа парсера"""
        Html = self.__getHTML()
        self.result = self.__getInf(Html)

    def __getHTML(self):
        """Получение HTML кода"""
        link = self.link
        return requests.get(link, headers=HEADERS)

    def __getInf(self, html):
        """Получение необходимой информации"""
        new_html = BS(html.text, "html.parser")
        array_of_inf = []
        All_element = new_html.find_all("div", class_="row1 index_cat_1st")
        All_element = All_element + new_html.find_all("div", class_="row2 index_cat_1st")
        link_base = "https://konferencii.ru/"
        for i in All_element:
            a = Global_dict()
            i = i.find("div", class_="index_cat_txt")
            # Достаем различные даты
            s = str(i.find("div", class_="left"))
            s = s.replace(" ", "")
            s = s[s.find('\n') + 1:]
            # Дата начала
            a.date_start = s[:s.find('.')]
            s = s[s.find('\n') + 1:]
            # Дата конца
            a.date_end = s[:s.find('.')]
            s = s[s.find('\n') + 1:]
            s = s[s.find('\n') + 1:]
            # Дата конца регистрации
            a.application_end = s[:s.find('.')]
            # Выгружаем ссылку и название
            s = str(i.find("div", class_="index_cat_tit").find("a"))
            s = s[s.find("=\"") + 2:]
            a.link = link_base + s[:s.find("\"")]
            a.Name = s[s.find(">") + 1:s.find("<")]
            # Выгружаем город и страну
            s = str(i.find("div", class_="left").find_next("div", class_="left").find("p", class_="ross_p").find("b"))
            a.Country = s[s.find(">") + 1:s.find(",")]
            a.city = s[s.find(",") + 2:s.rfind("<")]
            array_of_inf.append(a)
        return array_of_inf
