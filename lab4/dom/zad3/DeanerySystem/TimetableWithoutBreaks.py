from typing import List
from .lesson import Lesson
from .term import Term
from .day import Day
import re
from enum import Enum

class Action(Enum):
    DAY_EARLIER = 0
    DAY_LATER = 1
    TIME_EARLIER = 2
    TIME_LATER = 3


class TimetableWithoutBreaks():
    def __init__(self):
        self.__list = []

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        return (not self.busy(term)) and Lesson.isTermValid(term, fullTime)


    def get(self, term: Term) -> Lesson:
        for lesson in self.__list:
            if lesson.term == term:
                return lesson
        return None


    def busy(self, term: Term) -> bool:
        return self.get(term) != None

    def put(self, lesson: Lesson) -> bool:
        if(self.can_be_transferred_to(lesson.term, lesson.fullTime)):
            self.__list.append(lesson)
            return True
        return False

    def remove(self, term: Term):
        for i,lesson in enumerate(self.__list):
            if(lesson.term == term):
                self.__list.pop(i)
                return True
        return False

    def replace(self, lesson: Lesson):
        self.remove(lesson.term)
        return self.put(lesson)

    def parse(self, actions: List[str]) -> List[Action]:
        reg = re.compile(r'^d\+$|^t\+$|^d-$|^t-$')
        i = 0
        while i < len(actions):
            if reg.match(actions[i]):
                i += 1
            else:
                actions.pop(i)
        translate = {"d+":Action.DAY_LATER, 
            "d-":Action.DAY_EARLIER, 
            "t-":Action.TIME_EARLIER, 
            "t+":Action.TIME_LATER}
        result = []
        for each in actions:
            result.append(translate[each])
        return result                

    def perform(self, actions: List[Action]):
        for i in range(len(actions)):
            if(actions[i] == Action.DAY_EARLIER):
                self.__list[i%len(self.__list)].earlierDay()
            elif(actions[i] == Action.DAY_LATER):
                self.__list[i%len(self.__list)].laterDay()
            elif(actions[i] == Action.TIME_LATER):
                self.__list[i%len(self.__list)].laterTime()
            elif(actions[i] == Action.TIME_EARLIER):
                self.__list[i%len(self.__list)].earlierTime()


    def __str__(self):
        out = " "*20
        for i in range(0,7):
            out += "*" + TimetableWithoutBreaks.align(Day(i).readable())
        out += "\n" + "*"*(8*20+7) + "\n"
        start = Term.fromInt(480)
        end = Term.fromInt(570)
        for i in range(0,8):
            time = str(start)[:-5] + "-" + str(end)[:-5]
            out += TimetableWithoutBreaks.align(time)
            for j in range(0,7):
                lesson = self.get(Term.fromInt(int(start)+1440*j))
                if(lesson == None):
                    out += "*" + " "*20 
                else:
                    out += "*" + TimetableWithoutBreaks.align(lesson.name)
            start.reInt(int(start)+90)
            end.reInt(int(end)+90)
            out += "\n" + "*"*(8*20+7) + "\n"
        return out