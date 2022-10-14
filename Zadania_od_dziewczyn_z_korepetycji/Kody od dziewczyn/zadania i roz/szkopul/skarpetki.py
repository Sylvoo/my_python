a, b = map(int, input().split())

if a == b:
    print(a, 0)
else:
    y = max([a, b]) - min([a, b])
    if y % 2 == 0:
        y = int(y / 2)
    else:
        y = int((y - 1) / 2)
    print(min([a, b]), y)
