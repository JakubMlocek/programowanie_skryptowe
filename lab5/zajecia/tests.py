import unittest
from dealer import Dealer, Car, Client
from datetime import date
import sys
import io

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









class PrintingTest(TestPrint):
    def testClientPrint(self):
        client1 = Client(1,"jakub","sztocek","katowice")
        with self.assertStdout("""Imie: jakub
Naziwsko: katowice
Adres: katowice\n"""):
            print(client1)

    def testCarPrint(self):
        car1 = Car(1,"opel",40000,200,4,date.today(),date.today())
        with self.assertStdout("""ID: 1
Marka: opel 
Cena Sprzedazy: 40000 
Cena Wynajmu: 200 
Wynajety od: 2022-11-15 do: 2022-11-15\n"""):
            print(car1)

class BasicTest(unittest.TestCase):

    def testParseGarageInfoLine(self):
        self.assertEqual(Dealer.garage,[])

        tmpCar1 = Car(0,"opel",40000,200)
        self.assertTrue(Dealer.parseGarageInfoLine("opel:40000:200") == tmpCar1)

        tmpCar2 = Car(0,"opel",40000,200)
        Dealer.addParsedLineToGarage("opel:40000:200")
        self.assertTrue(Dealer.garage[0] == tmpCar2)

        tmpCar3 = Car(1,"suzuki",60000,350)
        Dealer.addParsedLineToGarage("suzuki:60000:350")
        self.assertTrue(Dealer.garage[1]== tmpCar3)

    def testSell(self):
        client0 = Client(0,"andrzej","monk","olkusz")
        client0 + Dealer.garage[1]
        self.assertEqual(Dealer.garage[1].identyfikator_klienta, client0.identyfikator_klienta)   

        client1 = Client(1,"jakub","sztocek","katowice")
        client1 + Dealer.garage[0]
        self.assertEqual(Dealer.garage[0].identyfikator_klienta, client1.identyfikator_klienta)   

    def testSellIfNotPossible(self):
        client1 = Client(1,"jakub","sztocek","katowice")
        client2 = Client(2,"konrad","macedonski","krakow")
        client2 + Dealer.garage[0]
        self.assertEqual(Dealer.garage[0].identyfikator_klienta, client1.identyfikator_klienta)   
        for car in Dealer.garage:
            car.identyfikator_klienta = None

    def testRent(self):
        client0 = Client(0,"andrzej","monk","olkusz")
        client0 << Dealer.garage[1]
        self.assertEqual(Dealer.garage[1].identyfikator_klienta, client0.identyfikator_klienta)   
        self.assertEqual(Dealer.garage[1].data_wypozyczenia, date.today())

        client1 = Client(1,"jakub","sztocek","katowice")
        client1 << Dealer.garage[0]
        self.assertEqual(Dealer.garage[0].identyfikator_klienta, client1.identyfikator_klienta)   
        self.assertEqual(Dealer.garage[0].data_wypozyczenia, date.today())


    def testRentIfNotPossible(self):
        client1 = Client(1,"jakub","sztocek","katowice")
        client2 = Client(2,"konrad","macedonski","krakow")
        client2 << Dealer.garage[0]
        self.assertEqual(Dealer.garage[0].identyfikator_klienta, client1.identyfikator_klienta)   

if __name__ == "__main__":
    unittest.main()