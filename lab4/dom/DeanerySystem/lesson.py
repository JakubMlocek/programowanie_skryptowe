from term import Term
from day import Day

class Lesson():
    def __init__(self, term :Term, name :str, teacherName :str, year :int) -> None:
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.fullTime = True