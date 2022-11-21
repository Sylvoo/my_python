r = int(input("Podaj promien okregu: "))

def skol_krat(r):
    if r == 0:
        wynik = 0
    else:
        wynik = (r+1)**2
    return wynik

print(skol_krat(r))