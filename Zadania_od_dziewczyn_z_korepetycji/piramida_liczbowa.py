n = int(input("Ile liczb: "))

ciag = []
for p in range(n):
    x = int(input("Podaj liczby do ciagu: "))
    ciag.append(x)

i = 1
while i <= n:
    for x in range(len(ciag) - 1):
        print(ciag[i-1])
        i += 1

# niedokonczone