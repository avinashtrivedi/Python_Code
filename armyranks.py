class Enlistee:
    def __init__(self, enlisteeName, enlisteeNumber):
        self.__enlisteeName = enlisteeName
        self.__enlisteeNumber = enlisteeNumber

    def set_enlisteeName(self,enlisteeName):
        self.__enlisteeName = enlisteeName

    def set_enlisteeNumber(self,enlisteeNumber):
        self.__enlisteeNumber = enlisteeNumber

    def get_enlisteeName(self):
        return self.__enlisteeName

    def get_enlisteeNumber(self):
        return self.__enlisteeNumber

       
class Private(Enlistee):
    def __init__(self, enlisteeName, enlisteeNumber, platoonNumber, serviceYears):
        Enlistee.__init__(self, enlisteeName, enlisteeNumber)
        self.__platoonNumber = platoonNumber
        self.__serviceYears = serviceYears

    def set_platoonNumber(self, platoonNumber):
        self.__platoonNumber = platoonNumber

    def set_serviceYears(self, serviceYears):
        self.__serviceYears = serviceYears

    def get_platoonNumber(self):
        return self.__platoonNumber

    def get_serviceYears(self):
        return self.__serviceYears