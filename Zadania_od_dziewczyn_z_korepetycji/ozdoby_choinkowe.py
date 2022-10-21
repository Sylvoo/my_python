import math

n = int(input("Ile ozdob: "))
k = int(input("Ile arkuszy w jednym zeszycie: "))
zeszyty = 0

czerw = 2
ziel = 5
nieb = 8

zapotrzeb_ark_czerw = n * czerw
zapotrzeb_ark_ziel = n * ziel
zapotrzeb_ark_nieb = n * nieb

zeszyt_czerw = math.ceil(zapotrzeb_ark_czerw/k)
zeszyt_ziel = math.ceil(zapotrzeb_ark_ziel/k)
zeszyt_nieb = math.ceil(zapotrzeb_ark_nieb/k)

wszystkie_zeszyty = zeszyt_czerw + zeszyt_ziel + zeszyt_nieb

print()
print(wszystkie_zeszyty)
print()
print(f'Kupujemy {zeszyt_czerw} zeszytow czerwonych, {zeszyt_ziel} zeszytow zielonych i {zeszyt_nieb} zeszytow niebieskich')







# ozdoba = 2czerwone 5ziel 8nieb





