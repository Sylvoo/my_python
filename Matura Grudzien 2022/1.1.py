
plik = open("mecz.txt", "r")  # WYNIK POPRAWNY 5030, rozni sie o 1 :/

wiersze = plik.readlines()

terazniejsza = " "
przeszla = " "
ile_razy = 0
for liczby in wiersze:
    for literka in liczby:
        terazniejsza = literka
        if terazniejsza != przeszla:
            ile_razy += 1
        przeszla = terazniejsza

print(ile_razy - 1)




