import random

znaki = 'abcdefghijklmnouprsqwtyzABCDEFGHIJKLMNOUPRSQWTYZ123456789!@#$%.'

dlugosc_hasla = 9
haslo = "".join(random.sample(znaki, dlugosc_hasla)) # "x".join(y)- wstawia "x" pomiedzy pojedyncze znaki w y
print(haslo)                                         # random.sample(x, ile)- zwraca randomowe znaki w zminnej x dana ilosc razy





