from Messengers.MessengerFactory import MessengersFactory
from Messengers.types import MessengersTokens
from Sites.MAI.utils import GetSchedule
from Sites.yandexWeather.yandexWeather import YandexWeather

apis = []

for messenger in MessengersTokens:
    token = MessengersTokens[messenger]
    apis.append(MessengersFactory.getMessengerApi(messenger, token))

while True:
    for api in apis:
        lastMessages = api.getLastMessages()

        for item in lastMessages:
            userId = item
            message = lastMessages[item][0]

            if message == 'расписание':
                weekSchedule = GetSchedule('8-Т3О-202Б-16', 1)

                for day in weekSchedule.days:
                    for subject in day.subjects:
                        api.sendMessage(userId, str(subject))
            elif message == 'python':
                api.sendMessage(userId, 'говнище')
            elif message == 'погода':
                res = YandexWeather.getWeather('moscow')
                api.sendMessage(userId, str(res))
            elif message == 'база данных':
                api.sendMessage(userId, 'В жопу ее ^^')
            else:
                api.sendMessage(userId, 'Хм хм хм... А я хз что тебе на это ответить')