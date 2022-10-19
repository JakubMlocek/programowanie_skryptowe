#!/usr/bin/python3
from sys import argv
import re
import getopt

if __name__ == "__main__":
    if len(argv) < 2:
        print("Dostepne opcje: --modul=[lista,slownik]")
    else:
        try:
            optlist, arg = getopt.getopt(argv[1:], "", "modul=")
        except getopt.GetoptError as e:
            print("Bład! Dostepne opcje: --modul=[lista,slownik]")
            exit()


        if(optlist[0][1] == "lista"):
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

        elif(optlist[0][1] == "slownik"):
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
            print("Dostepne opcje: --modul=[lista,slownik]")
