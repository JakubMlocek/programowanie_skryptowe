from .day import Day
from .term import Term 

class Lesson():
    def __init__(self, timetable, term :Term, name :str, teacherName :str, year :int) -> None:
        self.__timetable = timetable
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__fullTime = True

    @property
    def term(self):
        return self.__term
    
    @term.setter
    def term(self, term :Term):
        if Lesson.isTermValid(term, self.fullTime):
            self.__term = term
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name :str):
        self.__name = name


    @property
    def teacherName(self):
        return self.__teacherName
    
    @teacherName.setter
    def teacherName(self, teacherName :str):
        self.__teacherName=teacherName

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self,year :int):
        if year in range(1,6):
            self.__year = year
            return True
        return False

    @property
    def fullTime(self):
        return self.__fullTime

    @fullTime.setter
    def fullTime(self, fullTime):
        if type(fullTime) == type(True):
            self.__fullTime = fullTime
            return True
        return False

    def __str__(self):
        rodzaj_studiow = None
        if self.fullTime:
            rodzaj_studiow = "stacjonarne"
        else:
            rodzaj_studiow = "niestacjonarne"
        return f"{self.name} ({self.term}) \n{self.year} Rok Studia {rodzaj_studiow} \nProwadzacy: {self.teacherName} "

    @staticmethod
    def isTermValid(term, full_time):
        minutes = int(term)
        if(full_time):
            if(minutes < 4*1440):
                if(minutes % 1440 in range(480,1200-term.duration+1)):
                    return True
                else:
                    return False
            elif(minutes > 4*1440 and minutes < 5 * 1440 ):
                if(minutes % 1440 in range(480,(60*17)-term.duration+1)):
                    return True
                else:
                    return False
        else:
            if(minutes > 5*1440):
                if(minutes % 1440 in range(480,1200-term.duration+1)):
                    return True
                else:
                    return False
            elif(minutes > 4*1440 and minutes < 5 * 1440 ):
                if(minutes % 1440 in range(60*17,(1200)-term.duration+1)):
                    return True
                else:
                    return False
    
    def move(self, dist):
        from .TimetableWithoutBreaks import TimetableWithoutBreaks
        newMinutes = int(self.__term)+dist
        if(not newMinutes in range(0,7*1440)):
            return False
        if(self.__timetable.can_be_transferred_to(Term.fromInt(newMinutes), self.__fullTime)):
            self.__term.rebuildFromMinutes(newMinutes)
            return True
        return False 

    def earlierDay(self):
        return self.move(-1440)

    def laterDay(self):
        return self.move(+1440)

    def earlierTime(self):
        return self.move(-self.__term.duration)

    def laterTime(self):
        return self.move(self.__term.duration)


