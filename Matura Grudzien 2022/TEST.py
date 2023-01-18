plik = open("liczby_przyklad.txt", "r")

wiersze = plik.readlines()

def czy_pierw(k):
    ile = 0
    for a in range(2, k+1):
        if (k-1) % a == 0:
            ile += 1
    if ile <= 1:
        print(f'liczba pierwsza: {k-1}')



for liczba in wiersze:
    liczba = int(liczba)
    czy_pierw(liczba)
