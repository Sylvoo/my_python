plik = open("liczby_przyklad.txt", "r") # Dla przykladowych dziala, dla normalnych danych dlugo liczy i nie moze wyliczyc

wiersze = plik.readlines()

def czy_pierw(k):
    ile = 0
    for a in range(2, k+1):
        if k % a == 0:
            ile += 1
    if ile <= 1:
        return True

def ile_sposobow(x):
    ile = 0
    for a in range(2, x+1):
        for b in range(2, x+1):
            if a+b == x:
                if czy_pierw(a)==True and czy_pierw(b)==True:
                    ile +=1
    if ile > 1:
        ile = ile//2 # Bo sie powtarzaja np 2+3 i 3+2
    return ile

max = 0
min = 999999
for liczba in wiersze:
    liczba = int(liczba)
    print()
    ile_sposobow(liczba)
    if ile_sposobow(liczba) > max:
        max = ile_sposobow(liczba)
    print(f' maksimum: {max}')

    if ile_sposobow(liczba) < min:
        min = ile_sposobow(liczba)
    print(f' minimum: {min}')





