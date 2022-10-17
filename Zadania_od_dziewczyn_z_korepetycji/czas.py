
t = int(input("Podaj liczbe sekund do zamiany na godziny: "))

g = 0
m = 0

def na_minuty(x):
    m = x // 60
    k = m // 60
    g = k
    m = m - k * 60
    t = x - g * 3600 - m * 60
    print(f'{g} godz, {m} min , {t} sekund')

na_minuty(t)
'''

if s > 60:
    m = t // 60
    

if m > 60:
    g = m // 60

print(f'{g}godz {m}min {s}sekund')

'''