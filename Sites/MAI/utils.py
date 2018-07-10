from DataBase.dataBase import DataBase
from Sites.MAI.mai import Mai
from Sites.MAI.types import Day, Subject, Week


def GetSchedule(group: str, week: int):
    resultCheck = Mai.checkGroup(group)
    if not resultCheck:
        raise Exception('Unknown group')

    weekSchedule = DataBase.Functions.get_week_schedule(group, week)

    if len(weekSchedule) == 0:
        weekSchedule = Mai.getSchedule(group, week)

        groupId = DataBase.Functions.get_group_id(group)
        if groupId is None:
            groupId = DataBase.Functions.set_group(group)

        for day in weekSchedule.days:
            for subject in day.subjects:
                subjectId = DataBase.Functions.set_subject(subject.nameSubject,
                                                           subject.typeSubject,
                                                           subject.teacher,
                                                           subject.classroom,
                                                           subject.time)

                idDay = DataBase.Functions.set_day(day.day, subjectId, day.dayName)
                DataBase.Functions.set_week(week, groupId, idDay)
    else:
        lastDay = -1
        week = Week()
        day = None

        for i in range(len(weekSchedule)):
            item = weekSchedule[i]

            currentDay = int(item[0])
            dayName = item[1]

            if lastDay != currentDay:
                if not day is None:
                    week.addDay(day)
                day = Day(currentDay, dayName)

            subject = Subject(item[2], item[3], item[4], item[5], item[6])

            day.addSubject(subject)

            lastDay = currentDay

        week.addDay(day)
        weekSchedule = week

    return weekSchedule
