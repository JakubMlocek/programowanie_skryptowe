import unittest
from DeanerySystem.term import Term, BasicTerm, Break
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import TimetableWithBreaks, Observer   
timetable = None

class TimetableWithBreaksTest(unittest.TestCase):
    def test_breaks_str(self):
        breaks = [Break(9, 30, 5), Break(11, 5, 10), Break(12, 45, 5), Break(14, 20, 20), Break(16, 10, 5), Break(17, 45, 5), Break(19, 20, 5)]
        self.assertEqual(str(breaks[0]), "---")

    def test_creating_breaks(self):
        breaks = [Break(9, 30, 5), Break(11, 5, 10), Break(12, 45, 5), Break(14, 20, 20), Break(16, 10, 5), Break(17, 45, 5), Break(19, 20, 5)]
        self.assertTrue(breaks[0].getTerm().isEq(BasicTerm(9, 30, 5)))
        self.assertTrue(breaks[1].getTerm().isEq(BasicTerm(11, 5, 10)))

    def test_integral_TimetableWithBreaks(self):
        exceptCatcher = False
        breaks = [Break(9, 30, 5), Break(11, 5, 10), Break(12, 45, 5), Break(14, 20, 20), Break(16, 10, 5), Break(17, 45, 5), Break(19, 20, 5)]
        global timetable 
        timetable = TimetableWithBreaks(breaks)
        lessons = [Lesson(timetable, Term(8,0), "Kryptografia", "test", 1), 
        Lesson(timetable, Term(8,0,90,Day.TUE), "Sieci", "test", 1), 
        Lesson(timetable, Term(9,35,90,Day.FRI), "Fizyka Laby", "test", 1)]

        for i in lessons:
            timetable.put(i)
            i.attach(Observer())
        
        try:
            timetable.put(lessons[1])
        except ValueError:
            exceptCatcher = True
        self.assertTrue(exceptCatcher)

        actions = []

        exceptCatcher = False
        try:
            actions = timetable.parse(["d-", "dd+", "d+d", "d+"])
        except ValueError as e:
            exceptCatcher = True
            self.assertEqual("Translation " + "dd+" + " is incorrect", str(e) )

        actions = timetable.parse(["t+", "d+", "t-", "d+", "t+"])
        timetable.perform(actions)
        self.assertTrue(exceptCatcher)
        self.assertEqual(lessons[0].term.day, Day.TUE)
        self.assertEqual(lessons[0].term.hour, 8)
        self.assertEqual(lessons[1].term.hour, 8)
        self.assertEqual(lessons[1].term.day, Day.WED)
        Lesson.skipBreaks = True
        timetable.perform(actions)
        self.assertEqual(lessons[0].term.day, Day.WED)
        self.assertEqual(lessons[0].term.hour, 9)
        self.assertEqual(lessons[1].term.hour, 9)
        self.assertEqual(lessons[1].term.day, Day.THU)
        self.assertEqual(lessons[2].term.hour, 8)
    
class ExceptionTest(unittest.TestCase):
    def test_hour_exception(self):
        term = Term(12,34)
        
        buf = 0
        err = 27

        try:
            term.hour = err
        except ValueError as e:
            buf = int(str(e))
        self.assertEqual(buf, err)
    
    def test_minute_exception(self):
        term = Term(12,34)

        err = 63
        try:
            term.minute = err
        except ValueError as e:
            buf = int(str(e))
        self.assertEqual(buf, err)

    def test_duration_exception(self):
        term = Term(12,34)

        err = 1234
        try:
            term.duration = err
        except ValueError as e:
            buf = int(str(e))
        self.assertEqual(buf, err)
 
if __name__ == '__main__':
    unittest.main(exit=False)
    print(timetable)