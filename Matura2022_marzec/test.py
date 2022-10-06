
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

#galerie = {}

#for wiersz in wiersze:
 #   miasto = wiersz.split(' ')[1]
 #   galerie[miasto] = 0
# print(galerie)


#for wiersz in wiersze:
#    for liczba in wiersz[11:]:
      #  print()
       # print(liczba)

