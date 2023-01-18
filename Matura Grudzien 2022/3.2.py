plik = open("liczby.txt", "r") # dziala, oba dobre wyniki !!

wiersze = plik.readlines()

def czy_pierwsza(x):
    p = 0
    for a in range(2, x + 1):
        if x % a == 0:
            p += 1
    if p <= 1:
        return True


ile = 0
for wiersz in wiersze:
        x = int(wiersz) - 1
        if czy_pierwsza(x) == True :
            ile += 1

print(ile)



