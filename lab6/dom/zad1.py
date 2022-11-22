from inspect import signature as sig
import unittest

def argumenty(argsFromClass):
    def dec_argumenty(func):
        def wrap_argumenty(*args):
            #pobranie ilości potrzebnych argumentów
            numOfWillenArgs = len(list(sig(func).parameters))

            finalArgs = list(args)

            numOfGivernArgs = len(finalArgs) + len(argsFromClass)
            if numOfGivernArgs < numOfWillenArgs:
                raise TypeError(
                    f'{func.__name__} takes exactly {numOfWillenArgs-1}, only ({numOfGivernArgs-1} arguments given)')

            ctr = 0
            while len(finalArgs) < numOfWillenArgs:
                finalArgs.append(argsFromClass[ctr])
                ctr += 1

            func(*finalArgs) #*podaje elementy z tablicy po kolei

            # próbujemy podać kolejną zmienną spośród podanych dekoratorowi
            try:
                return argsFromClass[ctr]
            # jeżeli nie ma już dostępnych argumentów (nie udało się), zwracamy None
            except:
                return None

        return wrap_argumenty
    return dec_argumenty


class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]  

    def __setitem__(self, key, value):
        if(key == "suma"):
            self.argumentySuma = value
        elif(key == "roznica"):
            self.argumentyRoznica = value
    
    @argumenty(argumentySuma)
    def suma(self,a,b,c):
        return( "%d+%d+%d=%d" % (a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(self,x,y):
        return("%d-%d=%d" % (x,y,x-y))

class extest(unittest.TestCase):
    def test_suma_3arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2, 3), 4)

    def test_suma_2arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2), 5)

    def test_suma_1arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1), None)

    def test_suma_0arg(self):
        op = Operacje()
        with self.assertRaises(TypeError):
            op.suma()
    
    def test_roznica_2arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(2, 1), 4)

    def test_roznica_1arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(2), 5)

    def test_roznica_0arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(), 6)

    def test_zmiana_zawartosci(self):
        op=Operacje()
        op['suma']=[1,2]
        op['roznica']=[1,2,3]
        self.assertEqual(op.argumentySuma, [1,2])
        self.assertEqual(op.argumentyRoznica, [1,2,3])

if __name__ == '__main__':
    unittest.main(exit=False)
