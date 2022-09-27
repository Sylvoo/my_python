from traceback import print_tb


a = int(input("Choose numer: "))
b = int(input("Choose another number: "))

import math
w = math.sqrt(a + b)
print("Pierwiastkiem sumy tych dwoch liczb jest: ")
print(w)

print("Liczba a podniesiona do potegi liczby b to: ")
print(pow(a,b))

print("Liczba b podniesiona do potegi liczby a to: ")
print(pow(b,a))

