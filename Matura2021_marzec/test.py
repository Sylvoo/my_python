
plik = open("galerie_przyklad.txt", "r", encoding="utf-8")
# zawartosc = plik.read()
wiersze = plik.readlines()
kraje = {}

for wiersz in wiersze:
    kraj = wiersz.split(' ')
    print(kraj)
    liczby = [kraj[2:]]
  #  powierzchnie_lokalow = liczby[0]*liczby[1]
    print(liczby)



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














# for wiersz in wiersze:
 #   miasto = wiersz.split(' ')[1]
 #   galerie[miasto] = 0
# print(galerie)


#for wiersz in wiersze:
#    for liczba in wiersz[11:]:
      #  print()
       # print(liczba)

