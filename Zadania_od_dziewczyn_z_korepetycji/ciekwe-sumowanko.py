n = int(input("Podaj ile liczb chcesz dodac: "))

tab = []
p = 1
for x in range(n):
    k = int(input(f'Wypisz {p} liczbe ktore chcesz dodac: '))
    p += 1
    tab.append(k)

print(tab)

for i in tab:
    if i < 0 and i % 2 != 0:
        tab.remove(i)
print(tab)

w = 0
wynik = 0
for p in tab:
    wynik = wynik + tab[w]
    w += 1
print(wynik)


