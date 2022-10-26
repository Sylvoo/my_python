a, b = map(int, input("Podaj licznik i mianownik ulamka: ").split())
x, y = map(int, input("Podaj licznik i mianownik ulamka: ").split())

if a/b + x/y >= 1:
    print("Nie spelnione zalozenie!! ")
else:
    p = a * y + b * x
    q = b * y
    while p%2 == 0 and q%2 == 0:
        p = p/2
        q = q/2
    print(f'{p}/{q}')   # Zadanie nie redukuje ulamka ale, liczy dobrze

