
ile = int(input("Ile ulamkow chcesz podac: "))

ciag_liczb = []
ciag_wynikow = []


for x in range(ile):
    l = int(input("Podaj licznik: "))
    m = int(input("Podaj mianownik: "))
    wynik = l/m
    wyniki = round(wynik, 3)
    ciag_liczb.append(l)
    ciag_liczb.append(m)
    ciag_wynikow.append(wyniki)

print(ciag_liczb)
print(ciag_wynikow)

najwieksza = -999
for i in range(2, len(ciag_liczb), 2):
    ulamek = int(ciag_liczb[i])/int(ciag_liczb[i+1])
    if ulamek > najwieksza:
        najwieksza = ulamek
        print(najwieksza)
        print(ciag_liczb[i], ciag_liczb[i+1])
    



