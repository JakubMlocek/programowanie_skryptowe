#!/usr/bin/python3
 
import sys

def is_prime(n):
    for i in range(2,int(n/2)):
        if (n%i) == 0:
            return False
    return True

for each in sys.argv:
    try:
        each = int(each)
    except:
        continue
    
    if is_prime(each):
        print(f"liczba pierwsza!  {each}")
