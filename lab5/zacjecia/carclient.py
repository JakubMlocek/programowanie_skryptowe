from datetime import date

class Car():
    def __init__(self, identyfikator_auta: int, identyfikator_klienta: int, marka: str, cena_sprzedazy: int, cena_wypozyczenia: int, data_wypozyczenia: date, data_zwrotu: date) -> None:
        self.identyfikator_auta = identyfikator_auta
        self.identyfikator_klienta = identyfikator_klienta
        self.marka = marka
        self.cena_sprzedazy = cena_sprzedazy
        self.cena_wypozyczenia = cena_wypozyczenia
        self.data_wypozyczenia = data_wypozyczenia #Getter i setter to do
        self.data_zwrotu = data_zwrotu #Getter i setter to do



class Client():
    def __init__(self, identyfikator_klienta: int, imie: str, nazwisko: str, adres: str) -> None:
        self.identyfikator_klienta = identyfikator_klienta
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres

    def __str__(self) -> str:
        return f"Imie: {self.imie}\nNaziwsko: {self.nazwisko}\nAdres: {self.adres}"
    
    def __repr__(self) -> str:
        return f"Imie: {self.imie}\nNaziwsko: {self.nazwisko}\nAdres: {self.adres}"
