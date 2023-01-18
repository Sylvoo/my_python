
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
for wiersz in wiersze:
    wiersz = wiersz.strip()
    wiersz = int(wiersz)
    while wiersz != 0:
        if wiersz % n == 0:
            print(f'{wiersz}, {n}')
            wiersz = wiersz // n
        if wiersz % n != 0:
            n = n+1
            for k in range(2, wiersz):
                if wiersz / k != 1:
                    continue
                else:
                    wiersz = 0



#    if wiersz % n != 0:
#        n = n+1
#    elif wiersz % n == 0:
#        print(f'{wiersz}, {n}')



#for dupa in liczbaa:
#    n = 2
#    if dupa % n != 0:
#        n = n + 1
#        while dupa % n == 0:
#            print(f'{dupa / n}')

