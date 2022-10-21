ile = int(input("Ile  ulamkow: "))
ciag = []

for x in range(ile):
    l = int(input("Podaj licznik: "))
    ciag.append(l)
    m = int(input("Podaj mianownik: "))
    ciag.append(m)

print(ciag)

ulamki = len(ciag)//2
najwiekszy = -999
p = 0
for i in range(ulamki):
    ulamek = int(ciag[p])/int(ciag[p+1])
    p += 2
    print(ulamek)
    if najwiekszy < ulamek:
        najwiekszy = ulamek

print("Najwiekszy ulamek to: ")
print(najwiekszy)