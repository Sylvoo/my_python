
a = int(input(f'Podaj dlugosc 1 patyka: '))
b = int(input(f'Podaj dlugosc 2 patyka: '))
c = int(input(f'Podaj dlugosc 3 patyka: '))

#    x, y, z = map(int, input().split())

def czy_prostokatny(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        if a > b and a > c:
            if a * a == b * b + c * c:
                print("Trojkat prostokatny a wiec 1")
                return True
        elif b > a and b > c:
            if b * b == a * a + c * c:
                return True
        elif c > b and c > a:
            if c * c == b * b + a * a:
                return True
    else:
        return False

if a == b == c:
    print("Trojkat rownoboczny a wiec 2")
elif czy_prostokatny(a, b, c) == True:
     print("Trojkat prostokatny a wiec 1")
else:
    print("Bajtus nie moze zbudowac trojkata!")

