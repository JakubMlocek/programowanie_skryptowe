#marka:ilosc:cena sprzedazy:cena wypozyczenia za dzien
import argparse
from datetime import date

class Dealer():
    def __init__(self):
        self.garaz = {}
        self.kupujacy = {}

    def readDataFile(self, path):
        with open(path,"r") as data:
            for line in data:
                marka, dane = self.parseFileLine(line)
                self.garaz[marka] = dane
    
    def parseFileLine(self, linia):
        linia = linia.split(':')
        dane = {}
        marka = linia[0]
        dane["ilosc"] = int(linia[1])
        dane["cena_sprzedazy"] = int(linia[2])
        dane["cena_wypozyczenia"] = int(linia[3])
        return marka, dane

    def parseInputLine(self, linia):
            #["kierowca"] = linia[0]
            #["marka"] = linia[1]
            #["czynnosc"] = linia[2] 
            #if tranzakcja["czynnosc"] == "W":
            #    tranzakcja["data_wypozyczenia"] = linia[3] #dodaj datetime
            #    tranzakcja["data_zwrotu"] = linia[4] #dodaj datetime
        
        try:
            linia = linia.split(':')
            if linia[2] == "K": #K-kupno W-wynajem
                self.sell(linia)
            if linia[2] == "W":
                self.rent(linia)
        except:
            print("Błednie podane dane!")

    def readInput(self):
        while True:
            try:
                print("kto:marka:czynnosc:datawyp:datazwr")
                #marek:opel:W:10.10.10:11.10.10
                linia = input("Podaj dane oddzielone : ")
                self.parseInputLine(linia)
            except EOFError:
                break

    def calculate(self):
        for osoba, tranzakcje in self.kupujacy.items():
            print(f"Osoba: {osoba}")
            lacznyKoszt = 0
            for tranzakcja in tranzakcje:
                if tranzakcja[1] == "K":
                    cena = self.garaz[tranzakcja[0]]["cena_sprzedazy"]
                    lacznyKoszt += cena
                    print(f"Kupno samochodu marki {tranzakcja[0]} za {cena}")
                elif tranzakcja[1] == "W":
                    cena = (self.garaz[tranzakcja[0]]["cena_wypozyczenia"] * ((tranzakcja[3]-tranzakcja[2]).days))
                    lacznyKoszt += cena
                    print(f"Wynajem marki {tranzakcja[0]} od: {tranzakcja[2]} do {tranzakcja[3]} za {cena}")
            print(f"Razem Wydala: {lacznyKoszt}")
            print()
            print()
        print(f"Koncowa zawartosc garazu:")
        for marka, value in self.garaz.items():
            sztuk = value["ilosc"]
            print(f"{marka} sztuk {sztuk}")


    def sell(self, linia):
        if self.garaz[linia[1]]["ilosc"] > 1:
            self.garaz[linia[1]]["ilosc"] -= 1
            if linia[0] in self.kupujacy: #jezeli juz istniala tranzakcja z tym kierowca dodajemy tranzakcje do jego tanzakcji
                self.kupujacy[linia[0]].append(linia[1:])
            else:
                self.kupujacy[linia[0]] = []
                self.kupujacy[linia[0]].append(linia[1:])
        else:
            print(f"Brak wystarczajacych zasobow zeby obsuzyc tranzakcje: {linia}")
        

    def rent(self, linia):
        if self.garaz[linia[1]]["ilosc"] > 1:
            data = linia[3].split('.')
            linia[3] = date(int(data[2]),int(data[1]),int(data[0]))
            data = linia[4].split('.')
            linia[4] = date(int(data[2]),int(data[1]),int(data[0]))
            if linia[0] in self.kupujacy:
                self.kupujacy[linia[0]].append(linia[1:])
            else:
                self.kupujacy[linia[0]] = []
                self.kupujacy[linia[0]].append(linia[1:])
        else:
            print(f"Brak wystarczajacych zasobow zeby obsuzyc tranzakcje: {linia}")

if __name__ == "__main__":
    #parser = argparse.ArgumentParser("Welcome to Car Dealer!")
    #parser.add_argument("file", help="path to file", type=str, required=True)
    #args = parser.parse_args()
    
    dealership = Dealer()
    line1 = "marek:opel:W:10.10.2010:11.10.2010"
    line2 = "k"
    #line2 = "kamil:opel:K"
    line3 = "marek:fiat:K"

    path = "/Users/jakmlo/Desktop/studia/sem3/prog_skryptowe/lab4/zajecia/data.txt"
    dealership.readDataFile(path)

    dealership.parseInputLine(line1)
    dealership.parseInputLine(line2)
    dealership.parseInputLine(line3)
    print(dealership.garaz)
    print(dealership.kupujacy)
    dealership.calculate()
    #unittest.main(exit=False)
