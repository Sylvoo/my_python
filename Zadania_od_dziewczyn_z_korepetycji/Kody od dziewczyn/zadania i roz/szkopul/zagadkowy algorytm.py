x, y = map(int, input().split())

a = x
b = y
while a != b:
    if a > b:
        b += y
    else:
        a += x
print(a)
print("nww")