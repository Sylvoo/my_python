tab = []
n = int(input("ilosc liczb: "))
for i in range(n):
    x = int(input(" "))
    tab.append(x)
print(tab)

for j in tab:
    print(j, end=" ")
g = -1
for v in tab:
    print(tab[g], end=" ")
    g -= 1
