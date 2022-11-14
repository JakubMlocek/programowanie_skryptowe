from carclient import Car, Client

class Dealer():
    def __init__(self) -> None:
        pass

    def parseFileLine(self, linia):
        samochod = Car()
        linia = linia.split(':')
        samochod.marka = linia[0]
        samochod.cena_sprzedazy = int(linia[2])
        samochod.cena_wypozyczenia = int(linia[3])
        samochody = [samochod for i in range(int(linia[1]))
        return samochody
    
    def readDataFile(self, path):
        with open(path,"r") as data:
            for line in data:
                marka, dane = self.parseFileLine(line)
                self.garaz[marka] = dane