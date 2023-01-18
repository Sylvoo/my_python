plik = open("mecz.txt", "r")  # Idealnie obydwa przyklady :D

wiersze  = plik.readlines()

a = 0
b = 0

for ciag in wiersze:
    for litera in ciag:
        if litera == "A":
            a += 1
            if a >= 1000 and a - b >= 3:
                print(f"Pierwszego seta wygrala druzyna A, wynikiem: {a}:{b} ")
                break
        elif litera == "B":
            b += 1
            if b >= 1000 and b - a >= 3:
                print(f"Pierwszego seta wygrala druzyna A, wynikiem: {a}:{b} ")
                break



