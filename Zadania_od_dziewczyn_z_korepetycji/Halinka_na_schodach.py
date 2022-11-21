n = int(input("Ilosc liczb do wczytania: "))

ciag = []

for i in range(n):
    liczba = input("Wczytaj liczby: ")
    ciag.append(liczba)

ile = 0
schody = []
for x in ciag:
    if x == "1":
        ile += 1

for k in range(len(ciag) - 1):
    if ciag[k] == "1":
        p = ciag[k-1]
        schody.append(p) ## OSTATNI PRZYKLAD cos nie tak

print(ile)
print(schody)
