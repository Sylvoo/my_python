
plik = open("przyklad.txt", "r")

wiersze = plik.readlines()

# ZADANIE 4.1
print("ZADANIE 4.1")
tab = []
for wiersz in wiersze:
        wiersz = wiersz.strip()
        tab.append(wiersz)

w = 0
k = 0
for liczba in tab:
    if liczba[0] == liczba[int(len(liczba)) - 1]:
        if k == 0:
            print(liczba)
            k = k+1
        w = w + 1
print(w)

# ZADANIE 4.2
print()
print("ZADANIE 4.2")
n = 2
max_czynnikow = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    wiersz = int(wiersz)
    ile_czynnikow = 0
    print(f'///{wiersz}///')
    for x in range(2, wiersz):
        ile_czynnikow = 0
        while wiersz % x == 0:
            wiersz = wiersz / x
            print(f'{wiersz}, dzielnik: {x}')
            ile_czynnikow += 1
        if ile_czynnikow > max_czynnikow:
            max_czynnikow = ile_czynnikow
        if wiersz == 0:
            break


print(f'Wiersz XD {max_czynnikow}')


