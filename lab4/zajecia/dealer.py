#marka:ilosc:cena sprzedazy:cena wypozyczenia za dzien

class Dealer():

    def __init__(self):
        pass
    
    def parseFileLine(self, linia):
        linia = linia.split(':')
        samochod = {}
        samochod["marka"] = linia[0]
        samochod["ilosc"] = int(linia[1])
        samochod["cena_sprzedazy"] = int(linia[2])
        samochod["cena_wypozyczenia"] = int(linia[3])
        return samochod

    def parseInputLine(self, linia):
        linia = linia.split(':')
        try:
            kierowca = {}
            kierowca["kto"] = linia[0]
            kierowca["marka"] = linia[1]
            kierowca["czynnosc"] = linia[2] #K-kupno W-wynajem
            if kierowca["czynnosc"] == "W":
                kierowca["data_wypozyczenia"] = linia[3]
                kierowca["data_zwrotu"] = linia[4]
            return kierowca
        except:
            print("Blednie podane parametry! Musisz podac opowiednia liczbe parametrow oddzielonych :")
            return None

    def readInput(self):
        dane = []
        while True:
            try:
                #kto:marka:czynnosc:datawyp:datazwr
                #marek:opel:W:10.10.10:11.10.10
                linia = input("Podaj dane oddzielone : ")
                dane.append(self.parseInputLine(linia))
            except EOFError:
                break
        return dane


    def rent_car():
        pass

    def return_car():
        pass

    def sell_car():
        pass

d = Dealer()

print(d.parseFileLine("fiat:13:40000:150"))
print(d.readInput())