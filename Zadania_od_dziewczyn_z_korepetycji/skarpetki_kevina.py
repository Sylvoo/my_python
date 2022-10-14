# a,b

a = 2 # liczba czerwone skarpetki
b = 3 # liczba niebieskie skarpetki\
liczba_dni_rozne_skarpetki = 0
liczba_dni_takie_same_skarpetki = 0

while a > 0 and b > 0:
    a -= 1
    b -= 1
    liczba_dni_rozne_skarpetki += 1
if a == 0 and b >= 2:
    liczba_dni_takie_same_skarpetki += 1
    b -= 2
elif b == 0 and a >= 2:
    liczba_dni_takie_same_skarpetki += 1
    a -= 2


print(f'Rozne skarpetki: {liczba_dni_rozne_skarpetki} Takie same skarpetki: {liczba_dni_takie_same_skarpetki}')




