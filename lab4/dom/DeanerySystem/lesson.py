from DeanerySystem.day import Day
from DeanerySystem.term import Term 

class Lesson():
    def __init__(self, term :Term, name :str, teacherName :str, year :int) -> None:
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.fullTime = True

    def __str__(self):
        rodzaj_studiow = None
        if self.fullTime:
            rodzaj_studiow = "stacjonarne"
        else:
            rodzaj_studiow = "niestacjonarne"
        return f"{self.name} ({self.term}) \n{self.year} Rok Studia {rodzaj_studiow} \nProwadzacy: {self.teacherName} "

    def isTermValid(self, term, full_time):
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
    
    def earlierDay(self):
        try:
            newTerm = self.term.rebuildFromMinutes(int(self.term)-1440)
        except ValueError:
            newDay = Day(6)
            newTerm = Term(newDay, self.term.hour, self.term.minute, self.term.duration)
            
        if self.isTermValid(newTerm, self.fullTime):
            self.term = newTerm
            return True
        else:
            return False

    def laterDay(self):
        try:
            newTerm = self.term.rebuildFromMinutes(int(self.term)+1440)
        except ValueError:
            newDay = Day(0)
            newTerm = Term(newDay, self.term.hour, self.term.minute, self.term.duration)
            
        if self.isTermValid(newTerm, self.fullTime):
            self.term = newTerm
            return True
        else:
            return False

    def earlierTime(self):
        newTerm = self.term.rebuildFromMinutes(int(self.term)-self.term.duration)
        if self.isTermValid(newTerm, self.fullTime):
            self.term = newTerm
            return True
        else:
            return False

    def laterTime(self):
        newTerm = self.term.rebuildFromMinutes(int(self.term)+self.term.duration)
        if self.isTermValid(newTerm, self.fullTime):
            self.term = newTerm
            return True
        else:
            return False


