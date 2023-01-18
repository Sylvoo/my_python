plik = open("mecz.txt", "r")  # Idealnie obydwa przyklady :D

wiersze  = plik.readlines()

a = 0
b = 0
passa_a = 0
passa_b = 0
ile_Dobrych_pass = 0
kogo = " "
najdluzsza = 0
for ciag in wiersze:
    for liczba in ciag:
        if liczba == "A":
            if passa_b >= 10:
                ile_Dobrych_pass += 1
                if passa_b > najdluzsza:
                    najdluzsza = passa_b
                    kogo = "B"
            passa_b = 0
            passa_a += 1
        if liczba == "B":
            if passa_a >= 10:
                ile_Dobrych_pass += 1
                if passa_a > najdluzsza:
                    najdluzsza = passa_a
                    kogo = "A"
            passa_a = 0
            passa_b += 1



print(ile_Dobrych_pass)
print(najdluzsza, kogo)