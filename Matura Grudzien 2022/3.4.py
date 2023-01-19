plik = open("liczby_przyklad.txt", "r")

wiersze = plik.readlines()

tab = []

for liczba in wiersze:
    x = hex(int(liczba))
    tab.append(x)

n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
nA = 0
nB = 0
nC = 0
nD = 0
nE = 0
nF = 0

for hexa in tab:
    for k in hexa[2:]:
        if k == "0":
            n0 += 1
        if k == "1":
            n1 += 1
        if k == "2":
            n2 += 1
        if k == "3":
            n3 += 1
        if k == "4":
            n4 += 1
        if k == "5":
            n5 += 1
        if k == "6":
            n6 += 1
        if k == "7":
            n7 += 1
        if k == "8":
            n8 += 1
        if k == "9":
            n9 += 1
        if k == "A":
            nA += 1
        if k == "B":
            nB += 1
        if k == "C":
            nC += 1
        if k == "D":
            nD += 1
        if k == "E":
            nE += 1
        if k == "F":
            nF += 1

for p in range(0,10):
    print(f'{p}')

tabu = ["A","B","C","D","E","F"]

for q in tabu:
    print(f'{q}')

print()
print(n0)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)
print(nA)
print(nB)
print(nC)
print(nD)
print(nE)
print(nF)
