from datetime import date

class Car():
    def __init__(self, identyfikator_auta: int, marka: str, cena_sprzedazy: int, cena_wypozyczenia: int, identyfikator_klienta = None, data_wypozyczenia = None, data_zwrotu = None) -> None:
        self.__identyfikator_auta = identyfikator_auta
        self.__marka = marka
        self.__cena_sprzedazy = cena_sprzedazy
        self.__cena_wypozyczenia = cena_wypozyczenia
        self.identyfikator_klienta = identyfikator_klienta
        self.data_wypozyczenia = data_wypozyczenia #Getter i setter to do
        self.data_zwrotu = data_zwrotu #Getter i setter to do

    def __str__(self) -> str:
        return f"ID: {self.identyfikator_auta}\nMarka: {self.marka} \nCena Sprzedazy: {self.cena_sprzedazy} \nCena Wynajmu: {self.cena_wypozyczenia} \nWynajety od: {self.data_wypozyczenia} do: {self.data_zwrotu}"

    def __eq__(self, other: object) -> bool:
        return self.identyfikator_auta == other.identyfikator_auta and self.marka == other.marka

    @property
    def identyfikator_auta(self):
        return self.__identyfikator_auta
    
    @identyfikator_auta.setter
    def identyfikator_auta(self, id: int):
        if type(id) == int:
            self.__identyfikator_auta = id
            return True
        else:
            return False

    @property
    def marka(self):
        return self.__marka
    
    @marka.setter
    def marka(self, m: str):
        if type(m) == str:
            self.__marka = m
            return True
        else:
            return False


    @property
    def cena_sprzedazy(self):
        return self.__cena_sprzedazy
    
    @cena_sprzedazy.setter
    def cena_sprzedazy(self, cena: int):
        if type(cena) == int:
            self.__cena_sprzedazy = cena
            return True
        else:
            return False


    @property
    def cena_wypozyczenia(self):
        return self.__cena_wypozyczenia
    
    @cena_wypozyczenia.setter
    def cena_wypozyczenia(self, cena: int):
        if type(cena) == int:
            self.__cena_wypozyczenia = cena
            return True
        else:
            return False



class Client():
    def __init__(self, identyfikator_klienta: int, imie: str, nazwisko: str, adres: str) -> None:
        self.__identyfikator_klienta = identyfikator_klienta
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__adres = adres

    def __str__(self):
        return f"Fullname: {self.name} {self.surname}"

    def __add__(self, car: Car):
        if car.identyfikator_klienta == None:
            car.identyfikator_klienta = self.identyfikator_klienta
            Dealer.transactions.append(f"{self.imie:10} {self.nazwisko:12} kupil  {car.marka:18} id number: {car.identyfikator_auta:2}  za  {car.cena_sprzedazy}") 
            for client in Dealer.clients:
                if client.imie == self.imie and client.nazwisko == self.nazwisko:
                    return None
            Dealer.clients.append(self)  

    def __lshift__(self, car: Car):
        if  car.data_wypozyczenia is None:
            car.identyfikator_klienta = self.identyfikator_klienta
            car.data_wypozyczenia = date.today()
            Dealer.transactions.append(f"{self.imie:10} {self.nazwisko:12} wypozyczyl  {car.marka:18} id number: {car.identyfikator_auta:2}  w  {car.data_wypozyczenia}") 
            for client in Dealer.clients:
                if client.imie == self.imie and client.nazwisko == self.nazwisko:
                    return None
            Dealer.clients.append(self)   
        else:
            Dealer.transactions.append(f"{self.imie} {self.nazwisko} you can't borrow {car.marka}!")

    def __rshift__(self, car: Car):
        if car.data_wypozyczenia is not None and car.identyfikator_klienta == self.identyfikator_klienta:
            car.data_zwrotu = date.today()
            Dealer.transactions.append(f"{self.imie:10} {self.nazwisko:12} zwrocil  {car.marka:18}  id number: {car.identyfikator_auta:2}  w  {car.data_zwrotu}") 
        else:
            Dealer.transactions.append(f"{self.imie} {self.nazwisko} you can't borrow {car.marka}!")


    @property
    def identyfikator_klienta(self):
        return self.__identyfikator_klienta
    
    @identyfikator_klienta.setter
    def identyfikator_klienta(self, id: int):
        if type(id) == int:
            self.__identyfikator_klienta = id
            return True
        else:
            return False

    @property
    def imie(self):
        return self.__imie
    
    @imie.setter
    def imie(self, imie: str):
        if type(imie) == str:
            self.__imie = imie
            return True
        else:
            return False

    @property
    def nazwisko(self):
        return self.__nazwisko
    
    @nazwisko.setter
    def nazwisko(self, nazw: str):
        if type(nazw) == str:
            self.__nazwisko = nazw
            return True
        else:
            return False

    @property
    def adres(self):
        return self.__adres
    
    @adres.setter
    def nazwisko(self, adres: str):
        if type(adres) == str:
            self.__adres = adres
            return True
        else:
            return False
    

    def __str__(self) -> str:
        return f"Imie: {self.imie}\nNaziwsko: {self.nazwisko}\nAdres: {self.adres}"
    
    def __repr__(self) -> str:
        return f"Imie: {self.imie}\nNaziwsko: {self.nazwisko}\nAdres: {self.adres}"
        


class Dealer:
    garage = []
    clients = []
    transactions = []


    def __str__(self):
        for car in Dealer.garage:
            print(car)
        for client in Dealer.clients:
            print(client)
        for transaction in Dealer.transactions:
            print(transaction)
        return ''

    @staticmethod
    def parseGarageInfoLine(linia):
        #marka:cena sprzedazy:cena wypozyczenia za dzien:ilosc
        linia = linia.split(':')
        samochod = Car(len(Dealer.garage), linia[0], int(linia[1]), int(linia[2]))
        return samochod

    def addParsedLineToGarage(line):
        car = Dealer.parseGarageInfoLine(line)
        Dealer.garage.append(car)


    @staticmethod
    def parseGarageFile(path):
        garage = []
        with open(path, "r") as file:
            for line in file:
                line = line.split(':')
                ilosc = int(line[-1])
                for _ in range(ilosc):
                    garage.append(Dealer.parseGarageInfoLine(line))
        return garage



    @classmethod
    def parseInput(cls):
        #imie:nazwisko:adres:idsamochodu:Kupno/Wypozyczenie(K/W/Z):DataWypozyczenia:DataZwrotu
        linia = linia.split(':')
        klient = Client(len(Dealer.clients), linia[0], linia[1],linia[2])
        if linia[4] == "K":
            klient + Dealer.garage[3]
        elif linia[4] == "W":
            klient << Dealer.garage[3]
        elif linia[4] == "Z":
            klient >> Dealer.garage[3]

if __name__=='__main__':
    try:
        Dealer.garage = Dealer.parseGarageFile("data.txt")
        while True:
            Dealer.parseInput()
            
    except(EOFError):
        print(Dealer())

# Adam Kasielski 123 + Harry_Potter Rowling