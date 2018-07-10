import abc


class IMessenger:
    def __init__(self, token: str):
        self.token = token

    @abc.abstractmethod
    def sendMessage(self, userId, message: str):
        pass

    @abc.abstractmethod
    def getLastMessages(self):
        pass
