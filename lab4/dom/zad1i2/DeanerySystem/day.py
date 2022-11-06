import enum

class Day(enum.Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def readable(self):
        return {
        Day.MON : "Poniedziałek",
        Day.TUE : "Wtorek",
        Day.WED : "Środa",
        Day.THU : "Czwartek",
        Day.FRI : "Piątek",
        Day.SAT : "Sobota",
        Day.SUN : "Niedziela"
        }[self]
    
    

    def difference(self, day):
        diff = day.value - self.value
        if(diff > 4):
            diff -= 7
        elif(diff < -4):
            diff += 7
        return diff

def nthDayFrom(n, day):
    return Day((day.value + n)%7)

wtorek = Day(1)
print(wtorek.value)