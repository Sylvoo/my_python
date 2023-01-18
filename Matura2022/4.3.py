print("ZADANIE 4.3")

plik = open("przyklad.txt", "r")

wiersze = plik.readlines()

liczba_trojek = 0
for wiersz in wiersze:
    if len(wiersz) == 3:
        x = wiersz[0]
        y = wiersz[1]
        z = wiersz[2]
        print(x, y, z)
        if int(y) != 0 and int(x) != 0:
            if int(y) % int(x) == 0:
                if int(z) % int(y) == 0:
                    liczba_trojek += 1

    if len(wiersz) == 4:
        x = wiersz[0]
        y = wiersz[2]
        z = wiersz[1]
        print(x, y, z)
        if int(y) != 0 and int(x) != 0:
            if int(y) % int(x) == 0:
                if int(z) % int(y) == 0:
                    liczba_trojek += 1

    if len(wiersz) == 4:
        x = wiersz[1]
        y = wiersz[0]
        z = wiersz[2]
        print(x, y, z)
        if int(y) != 0 and int(x) != 0:
            if int(y)% int(x) == 0:
                if int(z)%int(y) == 0:
                    liczba_trojek += 1

    if len(wiersz) == 4:
        x = wiersz[1]
        y = wiersz[2]
        z = wiersz[0]
        print(x, y, z)
        if int(y) != 0 and int(x) != 0:
            if int(y)% int(x) == 0:
                if int(z)%int(y) == 0:
                    liczba_trojek += 1

    if len(wiersz) == 4:
        x = wiersz[2]
        y = wiersz[0]
        z = wiersz[1]
        print(x, y, z)
        if int(y) != 0 and int(x) != 0:
            if int(y) % int(x) == 0:
                if int(z) % int(y) == 0:
                    liczba_trojek += 1

    if len(wiersz) == 4:
        x = wiersz[2]
        y = wiersz[1]
        z = wiersz[0]
        print(x, y, z)
        if int(y) != 0 and int(x) != 0:
            if int(y) % int(x) == 0:
                if int(z) % int(y) == 0:
                    liczba_trojek += 1

print(liczba_trojek)




