import re

def splitter():
    while True:
        tekst = input()
        while tekst:
            poz = re.match('^\d+', tekst)
            if poz:
                tekst = tekst[poz.end():]
                print("Liczba:" + poz.group(0))
            poz = re.match('^\D+', tekst)
            if poz:
                tekst = tekst[poz.end():]
                print("Wyraz:" + poz.group(0))


def splitter_for_test(tekst):
    result=""
    while tekst:
        poz = re.match('^\d+', tekst)
        if poz:
            tekst = tekst[poz.end():]
            result+= f"Liczba:{poz.group(0)}"
        poz = re.match('^\D+', tekst)
        if poz:
            tekst = tekst[poz.end():]
            result+= f"Wyraz:{poz.group(0)}"
    return result

if __name__ == "__main__":
    splitter()