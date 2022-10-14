
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
    for i in range(2, len(informacje) - 1, 2):
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
print(f'Max galeria: {max_miasto} {max_powierzchnia} ')
print(f'Min galeria: {min_miasto} {min_powierzchnia} ')
print()

# Zadanie 4.3

max_roznych_lokali = 0
max_roznych_lokali_miasto = ''
min_roznych_lokali = 9999
min_roznych_lokali_miasto = ''

for wiersz in wiersze:
    informacje = wiersz.split(' ')
    miasto = informacje[1]
    rozne_lokale = set()
    for i in range(2, len(informacje) - 1, 2):
        if informacje[i] == '0':
            continue
        powierzchnia_lokalu = int(informacje[i]) * int(informacje[i + 1])
        rozne_lokale.add(powierzchnia_lokalu)

    if len(rozne_lokale) > max_roznych_lokali:
        max_roznych_lokali = len(rozne_lokale)
        max_roznych_lokali_miasto = miasto
    if len(rozne_lokale) < min_roznych_lokali:
        min_roznych_lokali = len(rozne_lokale)
        min_roznych_lokali_miasto = miasto

print('\nZadanie 4.3')
print(f'max roznych: {max_roznych_lokali_miasto} {max_roznych_lokali}')
print(f'min roznych: {min_roznych_lokali_miasto} {min_roznych_lokali}')
























