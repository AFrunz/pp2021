"""парсер самолетов"""


import requests
from bs4 import BeautifulSoup as BS
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.111 Safari/537.36', 'accept': '*/*', 'cookie': 'G_AUTHUSER_H=0; G_ENABLED_IDPS=google; _ga=GA1.1.1708452945.1603900516; G_AUTHUSER_H=0; df_id=93a48948b52daf05e4f48c9f0e15a37d; xf_user=3626977%2C5095f49fae7649341ebe39a668dc4d66fc2cf4a6; xf_logged_in=1; xf_session=736654ce9b5a156fdf2bf94a69c0265b; xf_market_items_viewed=8103659; xf_market_custom_cat_id=2; xf_market_search_url=%2Fmarket%3Fcategory_id%3D2%26_loadSearchBar%3Dtrue%26title%3D%26_xfRequestUri%3D%252Fmarket%252F%26_xfNoRedirect%3D1%26_xfToken%3D3626977%252C1604229396%252C385cb84b3d3bb290650e7a0e188a6514f1eafb89%26_xfResponseType%3Djson; _ga_J7RS527GFK=GS1.1.1604227707.6.1.1604229406.0'
           }


class plane_dict:
    """Информация о самолете"""
    def __init__(self):
        self.number = None
        #self.link = None - не получилось, проблема с парсингом
        self.port_iz = None
        self.port_v = None
        self.time_iz = None
        self.time_v = None
        self.rating = None
        self.price =None
        self.type = None

    def Print_s(self):
        print(self.number, self.port_iz, self.time_iz, self.port_v, self.time_v, self.rating, self.type)


class avia_parse:
    link = "https://www.kayak.ru/flights/MOW-LED/2021-03-02?sort=bestflight_a"

    def __init__(self, city_from, city_to, day, month):
        self.city_from = city_from
        self.city_to = city_to
        self.day = day
        self.month = month
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
        data = new_html.find_all("div", class_="resultWrapper")
        for i in data:
            a = plane_dict()
            """Заполняем словарь ценами"""
            s = i.find("span", class_="price-text")
            s = s.get_text()
            a.price = s[:-2].strip()
            """Заполняет компаниями"""
            s = i.find("span", class_="codeshares-airline-names")
            s = s.get_text()
            a.number = str(s).strip()
            """Заполняет аэропортами"""
            s = i.find_all("span", class_ = "airport-name")
            fn = str(s[0])
            fn = fn.replace("\n", "")
            fn = fn[1:]
            fn = fn[fn.find(">"):fn.find("<")]
            fn = fn[1:-1]
            a.port_iz = fn
            ln = str(s[1])
            ln = ln.replace("\n", "")
            ln = ln[1:]
            ln = ln[ln.find(">"):ln.find("<")]
            ln = ln[1:-1]
            a.port_v = ln
            """Время вылета"""
            s = i.find("span", class_="depart-time base-time")
            s = s.get_text()
            a.time_iz = s.split()
            """Время прилета"""
            sti = i.find("span", class_="arrival-time base-time")
            sti = sti.get_text()
            a.time_v = sti.split()
            """Рейтинг"""
            r = i.find("span", class_="_ial _idj _iaj")
            if r is None:
                r = -1
            else:
                r = r.get_text()
            a.rating = r
            array_of_inf.append(a)
        return array_of_inf


a = avia_parse(12,12,12,12)
c = a.getRes()
for i in c:
    print(i.price, i.number, i.port_iz, i.port_v, i.time_iz, i.time_v, i.rating)
