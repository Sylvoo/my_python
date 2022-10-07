
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
print('Zadanie 4.2a')

#Zadanie 4.2a

galerie = []
max_miasto = ''
max_powierzchnia = 0
min_miasto = ''
min_powierzchnia = 9999

for wiersz in wiersze:
    informacje = wiersz.split(' ')
    miasto = informacje[1]
    powierzchnia_galerii = 0
    liczba_lokali = 0
    for i in range(2, len(wiersz) - 1, 2):
        if informacje[i] == '0':
            break
        liczba_lokali += 1
        powierzchnia_lokalu = int(informacje[i]) * int(informacje[i+1])
        powierzchnia_galerii += powierzchnia_lokalu
    print(f'{miasto} {powierzchnia_galerii} {liczba_lokali}')


    if powierzchnia_galerii > max_powierzchnia:
        max_powierzchnia = powierzchnia_galerii
        max_miasto = miasto
    if powierzchnia_galerii < min_powierzchnia:
        min_powierzchnia = powierzchnia_galerii
        min_miasto = miasto

print()
print('Zadanie 4.2b')
print(f'{max_miasto} {max_powierzchnia} ')
print(f'{min_miasto} {min_powierzchnia} ')














