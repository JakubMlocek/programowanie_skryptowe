from day import Day


class Term():
    def __init__(self,day :Day, hour :int, minute :int) -> None:    
        self.hour = hour
        self.minute = minute
        self.duration = 90
        self.__day = day

    def __str__(self) -> str:
        return f"{self.__day.readable()} {self.hour}:{self.minute} [{self.duration}]" 

    def __int__(self):
        return (self.__day.value*1440+self.hour*60+self.minute)

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
