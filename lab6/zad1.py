from inspect import signature as sig

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

