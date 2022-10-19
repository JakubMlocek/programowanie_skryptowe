lista = []

def zapisz(liczba):
    exists = False
    for idx in range(len(lista)):
        if lista[idx][0] == liczba:
            lista[idx][1] += 1
            exists = True
    
    if not exists:
        lista.append([liczba,1])
        

def wypisz():
    for each in lista:
        print(f"{each[0]}:{each[1]}",end=", ")