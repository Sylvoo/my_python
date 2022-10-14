# 2 czerwone 5 zielonych 8 niebieskich
# zeszyt ma k arkuszy
# n = ilość ozdób
# k = ilość arkuszy w zeszycie

n, k = map(int, input().split())

ark = 0

cz = 2 *n
z = 5*n
n = 8*n

if cz%k == 0:
    ark = cz/k
else:
    ark = cz//k + 1

if z%k == 0:
    ark = ark + z/k
else:
    ark = ark + z//k + 1

if n%k == 0:
    ark = ark + n/k
else:
    ark = ark + n//k + 1

print(int(ark))
