class MedicalExamination(object):
    """docstring for MedicalExamination."""

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def report(self):
        return self.__report

    @report.setter
    def report(self, report):
        self.__report = report

    @property
    def doctor(self):
        return self.__doctor

    @doctor.setter
    def doctor(self, doctor):
        self.__doctor = doctor


    def __init__(self, id, date, type, report ,doctor):
        self.__id = id
        self.__date = date
        self.__type = type
        self.__report = report
        self.__doctor = doctor

    def __str__(self):
        return "\n".join([
            "{:>12}: {}".format("id", self.__id),
            "{:>12}: {}".format("date", self.__date),
            "{:>12}: {}".format("date", self.__date),
            "{:>12}: {}".format("type", self.__type)])
