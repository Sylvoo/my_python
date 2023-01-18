plik = open("pary.txt","r") # DOBRY WYNIK! dziala

wiersze = plik.readlines()


for liczba in wiersze:
    x = liczba.split()
    a = int(x[0])
    b = int(x[1])
    copy_b = b
    while a<b:
        b = b // 2
    if b == a:
        print(a, copy_b)


