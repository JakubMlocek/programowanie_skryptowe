import unittest
from DeanerySystem.lesson import Lesson
from DeanerySystem.term import Term
from DeanerySystem.day import Day, nthDayFrom
from DeanerySystem.TimetableWithoutBreaks import TimetableWithoutBreaks, Action

class DayTest(unittest.TestCase):

    def test_nth(self):
        self.assertEqual(nthDayFrom(1, Day.SAT), Day.SUN)
        self.assertEqual(nthDayFrom(2, Day.SAT), Day.MON)
        self.assertEqual(nthDayFrom(-1, Day.TUE), Day.MON)
        self.assertEqual(nthDayFrom(-2, Day.TUE), Day.SUN)

    def test_difference(self):
        self.assertEqual(Day.MON.difference(Day.TUE), 1)
        self.assertEqual(Day.MON.difference(Day.SUN), -1)
        self.assertEqual(Day.SUN.difference(Day.MON), 1)
        self.assertEqual(Day.SUN.difference(Day.SAT), -1)

class TermTest(unittest.TestCase):

    def test_earlierThan(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.TUE, 10, 15)
        term3 = Term(Day.SAT, 13, 10)
        term4 = Term(Day.SAT, 12, 10)
        self.assertEqual(term1.earlierThan(term2),True)
        self.assertEqual(term3.earlierThan(term2),False)
        self.assertEqual(term3.earlierThan(term4),False)

    def test_laterThan(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.TUE, 10, 15)
        term3 = Term(Day.SAT, 13, 10)
        term4 = Term(Day.SAT, 12, 10)
        self.assertEqual(term1.laterThan(term2),False)
        self.assertEqual(term3.laterThan(term2),True)
        self.assertEqual(term3.laterThan(term4),True)
    
    def test_equals(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.TUE, 10, 15)
        term3 = Term(Day.SAT, 13, 10)
        term4 = Term(Day.SAT, 13, 10)
        self.assertEqual(term1.equals(term2),False)
        self.assertEqual(term1.equals(term3),False)
        self.assertEqual(term3.equals(term4),True)
        self.assertEqual(term1.equals(term4),False)        

    def test_str(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.SAT, 13, 10)
        self.assertEqual(str(term1),"Wtorek 9:45 [90]")
        self.assertEqual(str(term2),"Środa 10:15 [90]")
        self.assertEqual(str(term3),"Sobota 13:10 [90]")

class LessonTest(unittest.TestCase):

    def testMovingHour(self):
        timetable = TimetableWithoutBreaks() 
        lesson = Lesson(timetable,Term(Day.TUE, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.laterTime()
        self.assertEqual(result, True)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Wtorek 10:10 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

        lesson = Lesson(timetable,Term(Day.TUE, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.earlierTime()
        self.assertEqual(result, True)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Wtorek 10:10 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

    def testMovingDay(self):
        timetable = TimetableWithoutBreaks() 
        lesson = Lesson(timetable,Term(Day.TUE, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.earlierDay()
        self.assertEqual(result, True)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Poniedziałek 8:40 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

        lesson = Lesson(timetable,Term(Day.MON, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.earlierDay()
        self.assertEqual(result, False)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Poniedziałek 8:40 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

        lesson = Lesson(timetable,Term(Day.TUE, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.laterDay()
        self.assertEqual(result, True)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Środa 8:40 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

class TimetableTest(unittest.TestCase):
    def testTimetable(self):
        timetable = TimetableWithoutBreaks()
        lesson = Lesson(timetable, Term(Day.MON,8,00), "Test", "Tester", 1)
        self.assertTrue(timetable.put(lesson))
        self.assertFalse(timetable.put(lesson))
        self.assertEqual(timetable.get(lesson.term),lesson)
        actions = timetable.parse(["d-", "dd+", "d+d", "d+"])
        self.assertEqual(actions, [Action.DAY_EARLIER, Action.DAY_LATER])
        timetable.perform(actions)
        self.assertTrue(timetable.busy(lesson.term))
        self.assertEqual(lesson.term.day, Day.TUE)
        lesson2 = Lesson(timetable, Term(Day.MON,9,30), "Test2", "Tester2", 1)
        timetable.put(lesson2)
        actions = timetable.parse(["d-", "d+", "t+", "t-"])
        timetable.perform(actions)
        self.assertEqual(int(lesson.term), (9*60+30))
        self.assertEqual(int(lesson2.term), (1440+8*60))
        print(timetable)


if __name__ == "__main__":
    unittest.main(exit=False)
    