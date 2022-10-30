import unittest
from DeanerySystem.term import Term
from DeanerySystem.day import Day 


class MiniTest(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()















"""
term1 = Term(Day.TUE, 9, 45)
print(term1)                     # Ma się wypisać: "Wtorek 9:45 [90]"
term2 = Term(Day.WED, 10, 15)
print(term2)                     # Ma się wypisać: "Środa 10:15 [90]"
print(term1.earlierThan(term2)); # Ma się wypisać: "True"
print(term1.laterThan(term2));   # Ma się wypisać: "False"
print(term1.equals(term2));      # Ma się wypisać: "False"
"""