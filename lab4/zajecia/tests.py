import unittest
from dealer import Dealer

class DealerTest(unittest.TestCase):
    pass


if __name__ == "__main__":
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
    #unittest.main(exit=False)