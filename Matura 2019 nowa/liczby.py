

file = open("przyklad.txt", "r")

wiersze = file.readlines()

potegi = []
for x in range(12):
    k = pow(3, x)
    potegi.append(k)

ile = 0
for wiersz in wiersze:
    liczba = int(wiersz)
    for x in potegi:
        if liczba == x:
            ile += 1

print("1)", ile)

def silnia(n): return n*silnia(n-1) if n > 1 else 1

liczby_silnia = []
for wiersz in wiersze:
    liczba = int(wiersz)
    wiersz = wiersz.strip()
    suma = 0
    for litera in wiersz:
        litera = int(litera)
        suma += silnia(litera)
    if suma == liczba:
        liczby_silnia.append(suma)

print("2)", liczby_silnia)






