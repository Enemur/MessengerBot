import bs4
import requests

from Sites.MAI.types import Week, Subject, Day


class _MaiClass:
    def __init__(self):
        self.__url = 'https://mai.ru'
        self.__scheduleUrl = self.__url + '/education/schedule'
        self.tmpUrl = 'https://mai.ru/education/schedule'

    def getSchedule(self, nameGroup: str, week: int = 1) -> Week:
        if not isinstance(week, int):
            raise Exception('week is not int')

        if week <= 0 or week > 18:
            raise Exception('incorrect input: week')

        url = '{0}/detail.php?group={1}&week={2}'.format(self.__scheduleUrl, nameGroup, week)
        html = requests.get(url).text

        parser = bs4.BeautifulSoup(html)
        days = parser.find_all('div', {'class': 'sc-table sc-table-day'})
        week = Week()

        for day in days:
            date = day.select_one('div.sc-table-col.sc-day-header.sc-gray')
            date = date.contents
            dayName = date[1].text
            numOfDay = date[0].split('.')[0]
            numOfDay = int(numOfDay)

            day = day.select_one('div.sc-table-col.sc-table-detail-container')
            subjects = day.select('div.sc-table-row')
            day = Day(numOfDay, dayName)

            for subject in subjects:
                time = subject.find('div', {'class': 'sc-table-col sc-item-time'}).text
                typeSubject = subject.find('div', {'class': 'sc-table-col sc-item-type'}).text
                nameSubject = subject \
                    .find('div', {'class': 'sc-table-col sc-item-title'}) \
                    .find('span', {'class': 'sc-title'}).text
                teacher = subject \
                    .find('div', {'class': 'sc-table-col sc-item-title'}) \
                    .find('a')

                if not teacher is None:
                    teacher = teacher.text

                classroom = subject \
                    .find('div', {'class': 'sc-table-col sc-item-location'})

                if not classroom is None:
                    classroom = classroom.text

                subject = Subject(time, typeSubject, nameSubject, teacher, classroom)
                day.addSubject(subject)

            week.addDay(day)

        return week

    def checkGroup(self, nameGroup: str):
        url = '{0}/detail.php?group={1}&week={2}'.format(self.__scheduleUrl, nameGroup, 1)
        html = requests.get(url).text

        parser = bs4.BeautifulSoup(html)
        days = parser.find_all('div', {'class': 'sc-table sc-table-day'})

        return len(days) > 0


Mai = _MaiClass()
