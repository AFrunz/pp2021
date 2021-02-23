import requests
from bs4 import BeautifulSoup as BS
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.111 Safari/537.36', 'accept': '*/*', 'cookie': 'G_AUTHUSER_H=0; G_ENABLED_IDPS=google; _ga=GA1.1.1708452945.1603900516; G_AUTHUSER_H=0; df_id=93a48948b52daf05e4f48c9f0e15a37d; xf_user=3626977%2C5095f49fae7649341ebe39a668dc4d66fc2cf4a6; xf_logged_in=1; xf_session=736654ce9b5a156fdf2bf94a69c0265b; xf_market_items_viewed=8103659; xf_market_custom_cat_id=2; xf_market_search_url=%2Fmarket%3Fcategory_id%3D2%26_loadSearchBar%3Dtrue%26title%3D%26_xfRequestUri%3D%252Fmarket%252F%26_xfNoRedirect%3D1%26_xfToken%3D3626977%252C1604229396%252C385cb84b3d3bb290650e7a0e188a6514f1eafb89%26_xfResponseType%3Djson; _ga_J7RS527GFK=GS1.1.1604227707.6.1.1604229406.0'
           }
class avia_parse():
    link = "https://www.onetwotrip.com/ru/f/search/2302MOWLED?sc=E&ac=1"

    def __init__(self, city_from, city_to, day, month):
        self.city_from = city_from
        self.city_to = city_to
        self.day = day
        self.month = month

    def get_Res(self):
        """Получение результатов парсинга"""
        pass

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


