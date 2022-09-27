
def silnia(liczba):
    if liczba  == 0: return 1
    return liczba * silnia(liczba - 1)

print(silnia(5))



