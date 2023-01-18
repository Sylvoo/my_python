import random

for ludzie in range(20):
    dzien = random.randint(1,30)
    miesiac = random.randint(1,12)
    rok = random.randint(1992,1997)
    if miesiac == 2:
        dzien = random.randint(1,28)

    print(dzien, miesiac, rok)


