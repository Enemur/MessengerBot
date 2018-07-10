class Subject:
    def __init__(self, time: str, typeSubject: str,
                 nameSubject: str, teacher: str, classroom: str):
        self.time = time
        self.typeSubject = typeSubject
        self.nameSubject = nameSubject
        self.teacher = teacher
        self.classroom = classroom

    def __str__(self):
        result = f'{self.time}\n{self.nameSubject} {self.typeSubject}\n'
        if not self.teacher is None:
            result += f'{self.teacher}\n'
        result += f'{self.classroom}'
        return result


class Day:
    def __init__(self, day: int, dayName: str):
        self.subjects: [Subject] = []
        self.day = day
        self.dayName = dayName

    def addSubject(self, subject: Subject):
        self.subjects.append(subject)


class Week:
    def __init__(self):
        self.days: [Day] = []

    def addDay(self, day: Day):
        self.days.append(day)
