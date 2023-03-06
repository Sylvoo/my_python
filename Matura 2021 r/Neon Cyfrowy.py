instrukcje = []
with open("instrukcje.txt") as f:
    for linia in f:
        instrukcja = linia.strip()
        instrukcje.append(instrukcja)

dlugosc = 0

for x in instrukcje:
    if x.startswith("DOPISZ"):
        dlugosc += 1
    elif x.startswith("USUN"):
        dlugosc -= 1

print("1)", dlugosc)

aktualny_rodzaj = None
aktualna_dl = 0
najdl_rodzaj = None
najdl_dl = 0

for x in instrukcje:
    rodzaj = x.split()[0]
    if aktualny_rodzaj == rodzaj:
        aktualna_dl += 1
        if aktualna_dl>najdl_dl:
            najdl_dl=aktualna_dl
            najdl_rodzaj = rodzaj
    else:
        aktualny_rodzaj = rodzaj
        aktualna_dl = 1

print("2)", najdl_rodzaj, najdl_dl)


litery = {}
for x in instrukcje:
    rodzaj, znak = x.split()
    if rodzaj == "DOPISZ":
        if znak in litery:
            litery[znak] += 1
        else:
            litery[znak] = 1
naj_litera = None
najczesciej = 0
for litera in litery:
    if litery[litera] > najczesciej:
        naj_litera = litera
        najczesciej = litery[litera]

print("3)", naj_litera, najczesciej)

napis = ""

for x in instrukcje:
    rodzaj, znak = x.split()
    if rodzaj == "DOPISZ":
        napis += znak
    elif rodzaj == "ZMIEN":
        napis = napis[:-1] + znak
    elif rodzaj == "USUN":
        napis = napis[:-1]
    elif rodzaj == "PRZESUN":
        if znak == "Z":
            nowy_znak = "A"
        else:
            kod_ascii = ord(znak)
            nowy_znak = chr(kod_ascii+1)
        napis = napis.replace(znak, nowy_znak,1)

print("4)", napis)





