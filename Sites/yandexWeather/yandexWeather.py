from datetime import datetime
import requests
import bs4

from Sites.yandexWeather.types import WeatherData


class YandexWeatherClass:
    def __init__(self):
        self.__url = 'https://yandex.ru/pogoda/'

    def getWeather(self, country: str):
        url = self.__url + country

        html = requests.get(url).text

        parser = bs4.BeautifulSoup(html)

        res = parser.find('div', {'class', 'temp fact__temp'})
        temp = res.contents[0].text

        res = parser.find('div', {'class', 'fact__props'})
        wind = res.find('dl', {'class', 'term term_orient_v fact__wind-speed'})
        wind = wind.contents[1].text
        dav = res.find('dl', {'class', 'term term_orient_v fact__pressure'})
        dav = dav.contents[1].text
        vl = res.find('dl', {'class', 'term term_orient_v fact__humidity'})
        vl = vl.contents[1].text

        typeWeather = parser.find('div', {'class', 'fact__condition day-anchor i-bem'}).text

        data = WeatherData(temp, wind, dav, vl, typeWeather, str(datetime.now()))

        return data


YandexWeather = YandexWeatherClass()
