
n = int(input("Podaj liczbe: "))

tab = []

for i in range(2, n+1):
    tab.append(i)
print(tab)

for x in tab:
    i = 2
    while n >= i * x:
        if i * x in tab:
            tab.remove(i*x)
        i += 1
print(tab)

