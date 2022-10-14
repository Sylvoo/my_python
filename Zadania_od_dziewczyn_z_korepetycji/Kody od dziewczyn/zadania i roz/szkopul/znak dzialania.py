a, b = map(int, input().split())

suma = a + b
iloczyn = a * b
roznica = a - b

tab = [suma, iloczyn, roznica]
if max[tab] == suma:
    print(a, "+", b, "=", suma)
elif max[tab] == iloczyn:
    print(a, "*", b, "=", iloczyn)
if max[tab] == suma:
    print(a, "-", b, "=", roznica)
