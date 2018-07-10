from Messengers import IMessenger
from Messengers.types import Messengers
from Messengers.vkontakte.vk import VkontakteClass


class MessengersFactory:
    @staticmethod
    def getMessengerApi(messenger: Messengers, token: str) -> IMessenger:
        if not isinstance(messenger, Messengers):
            raise Exception('messenger not type Messengers')

        if messenger == Messengers.vk:
            return VkontakteClass(token)