import math    # DZIALA !

a, b = map(int, input("Podaj dwie liczby: ").split())

def trzecia_pit(a, b):
    c2 = a*a + b*b
    c = float(math.sqrt(c2))
    print(f'{a} + {b} = {c} ')

    c2_2 = a*a - b*b
    if c2_2 > 0:
        c_2 = float(math.sqrt(c2_2))
        if b * b + c_2 * c_2 == a * a:
            print(f'{b} + {c_2} = {a}')
        else:
            print(0)
    else:
        print(0)


    c2_3 = b*b - a*a
    c_3 = float(math.sqrt(c2_3))
    if a*a + c_3 * c_3 == b * b:
        print(f'{a} + {c_3} = {b}')
    else:
        print(0)





trzecia_pit(a, b)

