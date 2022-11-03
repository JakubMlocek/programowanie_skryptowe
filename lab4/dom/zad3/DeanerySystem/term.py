from .day import Day
from math import floor

class Term():
    def __init__(self,day :Day, hour :int, minute :int, duration=None) -> None:    
        self.__hour = hour
        self.__minute = minute
        if duration is not None:
            self.__duration = duration
        else:
            self.__duration = 90
        self.__day = day

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration :int):
        if duration in range(0, 600):
            self.__duration = duration
            return True
        return False

    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day :Day):
        if type(day) == type(Day.MON):
            self.__day = day
            return True
        return False
    
    @property
    def minute(self):
        return self.__minute
    
    @minute.setter
    def minute(self, minute :int):
        if minute in range(0,60):
            self.__minute = minute
            return True
        return False

    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, hour :int):
        if hour in range(0,24):
            self.__hour = hour
            return True
        return False

    def __str__(self) -> str:
        return f"{self.__day.readable()} {self.hour}:{self.minute} [{self.duration}]" 

    def __int__(self):
        return (self.__day.value*1440+self.hour*60+self.minute)

    @classmethod
    def fromInt(cls, minutes:int):
        return Term(Day(floor(minutes/1440)), floor(minutes/60) - floor(minutes/1440)*24, minutes % 60)

    def rebuildFromMinutes(self, minutes:int):
        self.hour = floor(minutes/60) - floor(minutes/1440)*24
        self.minute = minutes % 60
        self.__day = Day(floor(minutes/1440))
        return self

    def earlierThan(self, termin):
        if int(self) < int(termin):
            return True
        else:
            return False

    def laterThan(self, termin):
        if int(self) > int(termin):
            return True
        else:
            return False
        
    def equals(self, termin):
        if int(self) == int(termin):
            if self.duration == termin.duration:
                return True
        return False

    def __lt__(self,term):
        return int(self) < int(term)
    
    def __le__(self, term):
        return int(self) <= int(term)

    def __ge__(self, term):
        return int(self) >= int(term)
    
    def __gt__(self,term):
        return int(self) > int(term)
    
    def __eq__(self,term):
        return int(self) == int(term) and self.duration == term.duration

    def __sub__(self,term):
        intSelf = int(self)
        intTerm = int(term) 
        newTerm = Term(term.__day, term.hour, term.minute)
        intSelf -= intTerm
        if(intSelf < 0):
            intSelf *= -1
        newTerm.duration = intSelf + self.duration
        return newTerm


