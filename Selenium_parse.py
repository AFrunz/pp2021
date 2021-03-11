"""Получение страницы с помощью селениума"""


from selenium import webdriver
import time


class fly_selenium:
    """Класс для получения страницы с помощью селениума"""
    def __init__(self, link):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        self.link = link
        self.__get_html()

    def get_res(self):
        """Возвращает HTML код"""
        # self.__get_html()
        return self.html

    def __get_html(self):
        """Получение HTML кода"""
        self.browser.get(self.link)
        time.sleep(20)
        self.html = self.browser.page_source
