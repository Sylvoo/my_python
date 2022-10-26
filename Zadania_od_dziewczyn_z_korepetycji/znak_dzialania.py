a, b = map(int, input("Podaj dwie liczby calkowite: ").split())

if a < 0 and b < 0:
    x = a - b
    y = a * b
    print(x)
    print(y)
    if x > y:
        print(f'{a} - {b} = {x} ')
    else:
        x = b - a
        print(f'({b}) * ({a}) = {y} ')

elif a < 0  and b > 0:
    x = b - a
    print(f'{b} - ({a})= {x} ')

elif a > 0 and b < 0:
    x = a - b
    print(f'{a} - ({b}) = {x} ')

elif a > 0 and b > 0:
    if a > b:
        x = a + b
        y = a * b
        if x > y:
            print(f'{a} + {b} = {x} ')
        else:
            print(f'{a} * {b} = {y} ')
    if b > a:
        x = a + b
        y = a * b
        if x > y:
            print(f'{a} + {b} = {x} ')
        else:
            print(f'{a} * {b} = {y} ')



