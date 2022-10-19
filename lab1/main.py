#!/usr/bin/python3
import sys
from fractions import Fraction

def sum(arg1, arg2):
    final1 = final2 = 0

    try:
        final1 = Fraction(arg1)
    except:
        pass
        
    try:
        final1 = complex(arg1)
    except:
        pass  
  
    try:
        final2 = Fraction(arg2)
    except:
        pass 
            
    try:
        final2 = complex(arg2)
    except:
       pass

    return final1 + final2

if __name__ == '__main__':
    print(f"suma = {sum(2,2)}")
    print(f"__name__ = {__name__}")
    print(type('Ala ma kota123'))