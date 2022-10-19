slownik = {}

def zapisz(liczba):
    if liczba in slownik:
        slownik[liczba] += 1
    else:
        slownik[liczba] = 1

def wypisz():
    for key, val in slownik.items():
        print(f"{key}:{val}",end=", ")