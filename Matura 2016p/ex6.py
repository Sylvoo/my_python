# ZADANIE 6.1
plik = open("dane6.txt", "r", encoding="utf-8")

tab = []
for i in plik:
    tab.append(int(i))

lp = []
ile = 0

for k in tab:
    x = 0
    for j in range(1, k):
        if k % j == 0:
            x += 1
    if x == 1:
        lp.append(k)
        ile += 1

print(f'Ilosc liczb pierwszych to: {ile}')

# ZADANIE 6.2
print(f'Najwieksza liczba pierwsza to: {max(lp)}')
print(f'Najmniejsza liczba pierwsza to: {min(lp)}')

# ZADANIE 6.3
i = 0
ilosc = 0
blizniacze = []

for q in lp:
    while i < len(lp) - 1:
        if abs(lp[i] - lp[i+1]) == 2:
            blizniacze.append(lp[i])
            blizniacze.append(lp[i+1])
            ilosc += 1
        i += 1


print(f'Ilosc blizniaczych liczb: {ilosc} ')
para = 0
print("Blizniacze liczby to: ")
for x in range(len(blizniacze)//2):
    print(blizniacze[para], blizniacze[para+1])
    para += 2











