
x, y = map(int, input("Podaj wspolrzedne punktu: ").split())



if x == 0 and y == 0:
    print("Punkt: [0,0]")
elif x == 0:
    print("Cwiartka: OY")
elif y == 0:
    print("Cwiartka: OX")
else:
    if x > 0 and y > 0:
        print("Cwiartka: I")
    elif x < 0 and y > 0:
        print("Cwiartka: II")
    elif x < 0 and y < 0:
        print("Cwiartka: III")
    elif x > 0 and y < 0:
        print("Cwiartka: IV")




