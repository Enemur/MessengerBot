def getFunctions(storedFunction):
    class Inner:
        @staticmethod
        @storedFunction
        def set_day(day: int, id_subject: int): pass

        @staticmethod
        @storedFunction
        def set_group(name: str): pass

        @staticmethod
        @storedFunction
        def set_subject(name: str, type: str, teacher: str, classroom: str, time: str): pass

        @staticmethod
        @storedFunction
        def set_week(week: int, id_group: int, id_day: int): pass

        @staticmethod
        @storedFunction
        def get_week_schedule(group: str, week: int): pass

        @staticmethod
        @storedFunction
        def get_group_id(group: str): pass

    return Inner
