from .term import Term
from .day import Day

class Lesson(object):
    skipBreaks = False
    @staticmethod
    def isTermValid(term, fullTime):
        minutes = int(term)
        if(fullTime):
            if(minutes < 4*1440):
                if(minutes % 1440 in range(480,1260-term.duration+1)):
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
                if(minutes % 1440 in range(480,1260-term.duration+1)):
                    return True
                else:
                    return False
            elif(minutes > 4*1440 and minutes < 5 * 1440 ):
                if(minutes % 1440 in range(60*17,(1260)-term.duration+1)):
                    return True
                else:
                    return False

    def __init__(self, timetable, term:Term, name:str, teacherName:str, year:int):
        self.__timetable = timetable
        if(int(term) < 1440*4+17*60-term.duration):
            self.__fullTime = True
        else:
            self.__fullTime = False
        if(Lesson.isTermValid(term, self.__fullTime)):
            self.__term = term
        else:
            self.__term = Term.rebuildFromMinutes(480)
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__observators = []
        
    def attach(self, observator):
        self.__observators.append(observator)

    def detach(self, observator):
        self.__observators.remove(observator)

    def notify(self):
        for each in self.__observators:
            each.update(self.__timetable)

    @property
    def term(self):
        return self.__term

    @property
    def name(self):
        return self.__name
    
    @property
    def teacherName(self):
        return self.__teacherName

    @property
    def year(self):
        return self.__year

    @property
    def fullTime(self):
        return self.__fullTime
    
    @term.setter
    def term(self, term):
        if(Lesson.isTermValid(term, self.__fullTime)):
            self.__term = term
            return True
        return False
        
    @name.setter
    def name(self, name):
        self.__name=name

    @teacherName.setter
    def teacherName(self, teacherName):
        self.__teacherName=teacherName

    @year.setter
    def year(self, year):
        if year in range(1,5):
            self.__year = year
            return True
        return False

    @fullTime.setter
    def fullTime(self, fullTime):
        if type(fullTime) == type(True):
            self.__fullTime = fullTime
            return True
        return False


    def __str__(self):
        output = self.__name + " (" + self.__term.dayAndHour() + ")\n"
        days = ["Pierwszy", "Drugi", "Trzeci", "Czwarty", "Piąty"]
        output += days[self.__year-1] + " rok studiów "
        if(self.__fullTime):
            output += "stacjonarnych\n"
        else:
            output += "niestacjonarnych\n"
        output += "Prowadzący: " + self.__teacherName + "\n"
        return output

    def move(self, dist):
        newMinutes = int(self.__term)+dist
        if(not newMinutes in range(0,7*1440)):
            return False
        if(self.__timetable.can_be_transferred_to(Term.rebuildFromMinutes(newMinutes), self.__fullTime)):
            #if hasattr(self.__timetable, 'dictionary'):
                #self.__timetable.dictionary.pop(int(self.term))
            self.__term.reInt(newMinutes)
                #self.__timetable.dictionary[int(self.term)] = self
            self.notify()
            #else:
             #   self.__term.reInt(newMinutes)
            return True
        if hasattr(self.__timetable, 'dictionary'):    
            raise ValueError
        return False 

    def earlierDay(self):
        return self.move(-1440)

    def laterDay(self):
        return self.move(+1440)

    def earlierTime(self):
        if(not Lesson.skipBreaks):
            return self.move(-self.__term.duration)
        else:
            return self.__timetable.transferrer(self, -1)

    def laterTime(self):
        if(not Lesson.skipBreaks):
            return self.move(+self.__term.duration)
        else:
            return self.__timetable.transferrer(self, 1)