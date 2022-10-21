r = int(input("Podaj dlugosc promienia: "))
import cmath
pole = cmath.pi * r *r

print(f'Pole jest rowne: {round(pole, 3)}')

obw = 2 * cmath.pi * r

print(f'Obw jest rowny: {round(obw, 3)}')

