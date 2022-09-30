# ZADANIE 4.1
plik = open("przyklad.txt", "r", encoding="utf-8")
# zawartosc = plik.read()
wiersze = plik.readlines()
ile = 0
pierwsza = -1

#for line in zawartosc:
#    print(line, end="")
# zawartosc = zawartosc.split("\n")
# list = [zawartosc]
# print(list)

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz[0] == wiersz[len(wiersz) - 1]:
        ile += 1
        if pierwsza == -1:
            pierwsza = wiersz

print("Zadanie 4.1.")
print(ile, pierwsza)

# ZADANIE 4.2
# 420 = 2 * 2 * 3 * 5 * 7
# 210-105-35-7-1
def rozklad_na_czynniki(liczba):
    czynniki = []
    i = 2
    while liczba > 1 and i * i <= liczba:
        while liczba % i == 0:
            czynniki.append(i)
            liczba = liczba / i
        i += 1

    if liczba > 1:
        czynniki.append(liczba)

    return czynniki

max_czynnikow = -1
max_czynnikow_liczba = -1
max_roznych_czynnikow = -1
max_roznych_czynnikow_liczba = -1

for wiersz in wiersze:
    liczba = int(wiersz)
    rozklad = rozklad_na_czynniki(liczba)

    if len(rozklad) > max_czynnikow:
        max_czynnikow = len(rozklad)
        max_czynnikow_liczba = liczba

    rozne = set(rozklad)
    if len(rozne) > max_roznych_czynnikow:
        max_roznych_czynnikow = len(rozne)
        max_roznych_czynnikow_liczba = liczba

print()
print("Zadanie 4.2.")
print(max_czynnikow_liczba,max_czynnikow, max_roznych_czynnikow_liczba, max_roznych_czynnikow)

# ZADANIE 4.3.

def ile_dobrych_trojek(wiersze):
    trojki = []
    for i in range(0, len(wiersze)):
        liczba_1 = int(wiersze[i])
        for j in range(0, len(wiersze)):
            if i == j:
                continue

            liczba_2 = int(wiersze[j])
            if liczba_2 % liczba_1 == 0:
                for k in range(0, len(wiersze)):
                    if i == k  or j == k:
                        continue

                    liczba_3 = int(wiersze[k])
                    if liczba_3 % liczba_2 == 0:
                        trojki.append([liczba_1, liczba_2, liczba_3])

    return trojki

dobre_trojki = ile_dobrych_trojek(wiersze)
print()
print('Zadanie 4.3.a')
print(len(dobre_trojki))

def ile_dobrych_piatek(wiersze):
    piatki = []
    for i in range(0, len(wiersze)):
        liczba_1 = int(wiersze[i])
        for j in range(0, len(wiersze)):
            if i == j:
                continue

            liczba_2 = int(wiersze[j])
            if liczba_2 % liczba_1 == 0:
                for k in range(0, len(wiersze)):
                    if i == k  or j == k:
                        continue

                    liczba_3 = int(wiersze[k])
                    if liczba_3 % liczba_2 == 0:
                        for n in range(0, len(wiersze)):
                            if i == n or k == n or j == n:
                                continue

                            liczba_4 = int(wiersze[n])
                            if liczba_4 % liczba_3 == 0:
                                for p in range(0, len(wiersze)):
                                    if i == p or k == p or j == p or n == p:
                                        continue

                                    liczba_5 = int(wiersze[p])
                                    if liczba_5 % liczba_4 == 0:
                                        piatki.append([liczba_1, liczba_2, liczba_3, liczba_4, liczba_5])
    return piatki

dobre_piatki = ile_dobrych_piatek(wiersze)
print()
print('Zadanie 4.3.b')
print(len(dobre_piatki))



































plik.close()



