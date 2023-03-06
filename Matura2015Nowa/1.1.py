plik = open("liczby.txt", "r", encoding="utf-8") # Dobry wynik

wiersze = plik.readlines()

ile = 0
for wiersz in wiersze:
    print(wiersz)
    print(len(wiersz))
    zero = 0
    for liczba in wiersz:
        if liczba == '0':
            zero += 1
        print(zero)
    if zero > (len(wiersz)-1)/2:
        ile += 1

print(ile)







