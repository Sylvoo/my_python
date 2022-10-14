# x,k,a

x = 6
k = 1
a = 2
dlugosc_drogi_adriana = 0
dlugosc_drogi_kozika = x
while dlugosc_drogi_adriana != dlugosc_drogi_kozika:
    dlugosc_drogi_adriana += 2
    dlugosc_drogi_kozika -= 1
    k = 1
    print(f'Krok: {k}')
    k = k + 1
    print(dlugosc_drogi_kozika)
    print(dlugosc_drogi_adriana)

    if dlugosc_drogi_kozika == dlugosc_drogi_adriana:
        print(f'Wygrany to: {1}')
    elif dlugosc_drogi_adriana == dlugosc_drogi_kozika:
        print(f'Wygran to: {0}')

