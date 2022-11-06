import unittest
from DeanerySystem.lesson import Lesson
from DeanerySystem.term import Term
from DeanerySystem.term import Day

class LessonTest(unittest.TestCase):

    def testMovingHour(self):
        lesson = Lesson(Term(Day.TUE, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.laterTime()
        self.assertEqual(result, True)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Wtorek 10:10 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

        lesson = Lesson(Term(Day.TUE, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.earlierTime()
        self.assertEqual(result, True)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Wtorek 10:10 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

    def testMovingDay(self):
        lesson = Lesson(Term(Day.TUE, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.earlierDay()
        self.assertEqual(result, True)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Poniedziałek 8:40 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

        lesson = Lesson(Term(Day.MON, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.earlierDay()
        self.assertEqual(result, False)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Poniedziałek 8:40 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

        lesson = Lesson(Term(Day.TUE, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        result = lesson.laterDay()
        self.assertEqual(result, True)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Środa 8:40 [90]) 
2 Rok Studia stacjonarne 
Prowadzacy: Stanisław Polak """) 

if __name__ == "__main__":
    unittest.main()