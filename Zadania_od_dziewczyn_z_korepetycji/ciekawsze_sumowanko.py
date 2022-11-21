n = int(input("Podaj ilosc paskow: "))

lista = []
for x in range(n):
    l = input("Podaj liczby znajdujace sie na pasku: ").strip(' ')
    lista.append(l)
print(lista)

wynik = 0
p = 0
for i in lista:
    wynik = wynik + int(lista[p])   # nie dziala
    p += 1

print(wynik)