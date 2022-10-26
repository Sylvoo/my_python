a, b, c = map(int, input("Podaj trzy liczby calkowite: ").split())

ciag = []
if a < b:
    while a <= b:
        ciag.append(a)
        a += c
else:
    while a > b:
        ciag.append(b)
        b += c

print(ciag)

'''
if a < b:
    x = b - a
    for i in range(abs(x)):
        print(a)
        a += 1
'''



