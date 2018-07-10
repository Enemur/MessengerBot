from Messengers.IMessenger import IMessenger
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


class VkontakteClass(IMessenger):
    def __init__(self, token: str):
        super().__init__(token)

        self.__session = vk_api.VkApi(token=token)
        self.__vkApi = self.__session.get_api()
        self.__longpoll = VkLongPoll(self.__session)

    def sendMessage(self, userId, message: str):
        self.__vkApi.messages.send(user_id=userId, message=message)

    def getLastMessages(self):
        result = {}
        events = self.__longpoll.check()

        for event in events:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.user_id in result:
                    result[event.user_id].append(event.text)
                else:
                    result[event.user_id] = [event.text]
        return result
