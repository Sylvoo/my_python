
plik = open("galerie_przyklad.txt", "r", encoding="utf-8")
# zawartosc = plik.read()
wiersze = plik.readlines()

#Zadanie 4.1

kraje = {}

for wiersz in wiersze:
    kraj = wiersz.split(' ')[0]
    kraje[kraj] = 0

for wiersz in wiersze:
    kraj = wiersz.split(' ')[0]
    kraje[kraj] = kraje[kraj] + 1

print('Zadanie 4.1: ')    # wypisywanie petla wyniku
for wartosc in kraje.keys():
    print(f'{wartosc}: {kraje[wartosc]}') #1 f'{}: {}:' - w taki sposob mozemy mieszac tekst i zmienne
    #2 NAZWA: formatowanie print(f'{}: {}:')
print()


#Zadanie 4.2a

galerie = {}

for wiersz in wiersze:
    miasto = wiersz.split(' ')[1]
    galerie[miasto] = 0
print(galerie)
print()

def jaka_powierzchnia(wiersze):
    lokal = []
    for wiersz in wiersze:
        wymiary = wiersz.split(' ')[2:]
       # print(wymiary)
        k = wymiary
        wymiary = list(map(int, k)) # Zamiana STR na INT w tablicy
        wymiar = wymiary[0] * wymiary[1]
        print(wymiary[0])
        print(wymiary[1])
        lokal.append(wymiar)
        print(lokal)



    print(wymiary[0])
    print(wymiary[1])
    print(wymiar)
#      for x in wymiary:
#        suma = wymiary[x] + wymiary[x+1]
#        k.append(suma)
#
#        print(k)



powierzchnia = {1}

for wiersz in wiersze:
    miasto = wiersz.split(' ')[1]


jaka_powierzchnia(wiersze)


















