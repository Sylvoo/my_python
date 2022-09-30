import math

from math import*

n = int(input("Podaj liczbe: "))

def czy_pierwsza(n):
    for i in range(2, int(sqrt(n)) +1):
        if n % i == 0:
            return False
        else:
            return True

print(czy_pierwsza(n))

