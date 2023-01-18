print("ZADANIE 4.3")

plik = open("przyklad.txt", "r")

tab =[]
wiersze = plik.readlines()
for k in wiersze:
    k = k.split()
    tab.append(k)

liczba_trojek = 0
for wiersz in tab:
    print(wiersz)
    if len(wiersz) == 3:
        print(len(wiersz))
        x = wiersz[0]
        y = wiersz[1]
        z = wiersz[2]
        print(x, y, z)
        if int(y) != 0 and int(x) != 0:
            if int(y) % int(x) == 0:
                if int(x)*int(y) == int(z):
                    liczba_trojek += 1


print(liczba_trojek)