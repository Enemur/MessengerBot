from threading import Lock
import mysql.connector
from DataBase.functions import getFunctions


class _DataBase:
    def __connect(self):
        self.__db = mysql.connector.connect(host='localhost', database='schedule',
                                           user='root', password='')
        if self.__db.is_connected():
            self.__cursor = self.__db.cursor()

    def __init__(self):
        self.__connect()
        self.__mutex = Lock()
        self.__functions = getFunctions(self.decorate())

    @property
    def Functions(self):
        return self.__functions

    def decorate(self):
        def getFuncDecorator(storedFunction):
            def callProcedure(*args):
                self.__mutex.acquire()
                try:

                    if not (self.__db.is_connected()):
                        self.__connect()

                    self.__cursor.callproc(storedFunction.__name__, args)
                    result = []

                    for item in self.__cursor.stored_results():
                        for item2 in item.fetchall():
                            result.append(item2)

                    if len(result) == 1 and len(result[0]) == 1:
                        result = result[0][0]
                    elif len(result) == 0:
                        rsult = None


                    self.__db.commit()

                finally:
                    self.__mutex.release()
                return result

            return callProcedure

        return getFuncDecorator


DataBase = _DataBase()