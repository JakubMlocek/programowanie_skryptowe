#!/usr/bin/python3
from sys import argv
import re

if __name__ == "__main__":
    if len(argv) < 2:
        print("Dostepne opcje: --lista, --slownik")
    elif(argv[1] ==  "--lista"):
        import lista
        tekst = input("Pisz sobie:")
        while tekst:
            poz = re.match('^\d+', tekst)
            if poz:
                tekst = tekst[poz.end():]
                lista.zapisz(poz.group(0))
            poz = re.match('^\D+', tekst)
            if poz:
                tekst = tekst[poz.end():]

        lista.wypisz()
    elif(argv[1] ==  "--slownik"):
        import slownik
        tekst = input("Pisz sobie:")
        while tekst:
            poz = re.match('^\d+', tekst)
            if poz:
                tekst = tekst[poz.end():]
                slownik.zapisz(poz.group(0))
            poz = re.match('^\D+', tekst)
            if poz:
                tekst = tekst[poz.end():]
        slownik.wypisz()
    else:
        print("Dostepne opcje: --lista, --slownik")
