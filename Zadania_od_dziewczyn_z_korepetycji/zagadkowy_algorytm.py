x, y = map(int, input("Podaj x, y : ").split())

a = x
b = y

def liczby(a, b):
    while True:
        if a == b:
            print(a)
            break
        elif a > b:
            b += y
            liczby(a,b)
        elif b > a:
            a += x
            liczby(a,b)   # wypisuje za duzo razy idk

liczby(x,y)
