
def pole_okregu():
    import math
    r = int(input("Podaj dlugosc promienia okregu: "))
    if r < 0:
        print("Promien nie moze byc liczba ujemna !")
    else:
        p = math.pi * r * r
        print("Pole okregu jest rowne: ")
        print(p)
    

pole_okregu()