import unittest
from dealer import Dealer
import io
import sys

# extend unittest.TestCase with new functionality
class TestPrint(unittest.TestCase):

    def assertStdout(self, expected_output):
        return _AssertStdoutContext(self, expected_output)

    # as a bonus, this syntactical sugar becomes possible:
    def assertPrints(self, *expected_output):
        expected_output = "\n".join(expected_output) + "\n"
        return _AssertStdoutContext(self, expected_output)

class _AssertStdoutContext:

    def __init__(self, testcase, expected):
        self.testcase = testcase
        self.expected = expected
        self.captured = io.StringIO()

    def __enter__(self):
        sys.stdout = self.captured
        return self

    def __exit__(self, exc_type, exc_value, tb):
        sys.stdout = sys.__stdout__
        captured = self.captured.getvalue()
        self.testcase.assertEqual(captured, self.expected)


class DealerTest(unittest.TestCase):
    
    def test_parseInputLine(self):
        dealership = Dealer()
        path = "/Users/jakmlo/Desktop/studia/sem3/prog_skryptowe/lab4/zajecia/data.txt"
        dealership.readDataFile(path)

        line1 = "marek:opel:W:10.10.2010:11.10.2010"
        line2 = "kamil:opel:K"

        dealership.parseInputLine(line1)
        dealership.parseInputLine(line2)
        self.assertEqual(dealership.garaz,{'fiat': {'ilosc': 13, 'cena_sprzedazy': 40000, 'cena_wypozyczenia': 150}, 'opel': {'ilosc': 12, 'cena_sprzedazy': 55000, 'cena_wypozyczenia': 200}, 'ferrati': {'ilosc': 2, 'cena_sprzedazy': 440000, 'cena_wypozyczenia': 900}, 'mustang': {'ilosc': 5, 'cena_sprzedazy': 100000, 'cena_wypozyczenia': 500}})

        line3 = "marek:fiat:K"
        dealership.parseInputLine(line3)
        self.assertEqual(dealership.garaz, {'fiat': {'ilosc': 12, 'cena_sprzedazy': 40000, 'cena_wypozyczenia': 150}, 'opel': {'ilosc': 12, 'cena_sprzedazy': 55000, 'cena_wypozyczenia': 200}, 'ferrati': {'ilosc': 2, 'cena_sprzedazy': 440000, 'cena_wypozyczenia': 900}, 'mustang': {'ilosc': 5, 'cena_sprzedazy': 100000, 'cena_wypozyczenia': 500}})

    def test_sell(self):
        dealership = Dealer()
        path = "/Users/jakmlo/Desktop/studia/sem3/prog_skryptowe/lab4/zajecia/data.txt"
        dealership.readDataFile(path)

        line2 = "kamil:opel:K"

        dealership.sell(line2.split(':'))
        self.assertEqual(dealership.garaz,{'fiat': {'ilosc': 13, 'cena_sprzedazy': 40000, 'cena_wypozyczenia': 150}, 'opel': {'ilosc': 12, 'cena_sprzedazy': 55000, 'cena_wypozyczenia': 200}, 'ferrati': {'ilosc': 2, 'cena_sprzedazy': 440000, 'cena_wypozyczenia': 900}, 'mustang': {'ilosc': 5, 'cena_sprzedazy': 100000, 'cena_wypozyczenia': 500}})

        line3 = "marek:fiat:K"
        dealership.sell(line3.split(':'))
        self.assertEqual(dealership.garaz, {'fiat': {'ilosc': 12, 'cena_sprzedazy': 40000, 'cena_wypozyczenia': 150}, 'opel': {'ilosc': 12, 'cena_sprzedazy': 55000, 'cena_wypozyczenia': 200}, 'ferrati': {'ilosc': 2, 'cena_sprzedazy': 440000, 'cena_wypozyczenia': 900}, 'mustang': {'ilosc': 5, 'cena_sprzedazy': 100000, 'cena_wypozyczenia': 500}})

        #line4 = "marek:suzuki:K"
        #self.assertEqual(dealership.sell(line4.split(':')),None)



class DealerTestIntegral(TestPrint):
    def test_integral_basic(self):
        dealership = Dealer()
        line1 = "marek:opel:W:10.10.2010:11.10.2010"

        path = "/Users/jakmlo/Desktop/studia/sem3/prog_skryptowe/lab4/zajecia/data.txt"
        dealership.readDataFile(path)

        dealership.parseInputLine(line1)
        dealership.calculate() 

        with self.assertStdout("""
PODSUMOWANIE:
Osoba: marek
Wynajem marki opel od: 2010-10-10 do 2010-10-11 za 200
Razem Wydala: 200


Koncowa zawartosc garazu:
fiat sztuk 13
opel sztuk 13
ferrati sztuk 2
mustang sztuk 5\n"""):
            dealership.calculate()

    def test_integral(self):
        dealership = Dealer()
        line1 = "marek:opel:W:10.10.2010:11.10.2010"
        line2 = "kamil:opel:K"
        line3 = "marek:fiat:K"
        line4 = "adnrzej:fiat:W:10.9.2010:20.9.2010"

        path = "/Users/jakmlo/Desktop/studia/sem3/prog_skryptowe/lab4/zajecia/data.txt"
        dealership.readDataFile(path)

        dealership.parseInputLine(line1)
        dealership.parseInputLine(line2)
        dealership.parseInputLine(line3)

        dealership.parseInputLine(line4)
        dealership.calculate()

        with self.assertStdout("""
PODSUMOWANIE:
Osoba: marek
Wynajem marki opel od: 2010-10-10 do 2010-10-11 za 200
Kupno samochodu marki fiat za 40000
Razem Wydala: 40200


Osoba: kamil
Kupno samochodu marki opel za 55000
Razem Wydala: 55000


Osoba: adnrzej
Wynajem marki fiat od: 2010-09-10 do 2010-09-20 za 1500
Razem Wydala: 1500


Koncowa zawartosc garazu:
fiat sztuk 12
opel sztuk 12
ferrati sztuk 2
mustang sztuk 5\n"""):
            dealership.calculate()




if __name__ == "__main__":   
    unittest.main(exit=False)


