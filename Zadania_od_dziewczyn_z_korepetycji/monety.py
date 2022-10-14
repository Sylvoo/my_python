# n, ciag n liczb

n = int(input("Podaj liczbę monet: "))
ciag = []
awers = 0
rewers = 0
for i in range(n):
    x = int((input(f'Podaj strone monety, rewers-1, awers-0: ')))
    ciag.append(x)
    if x == 1:
        rewers += 1
    elif x == 0:
        awers += 1

print(f'Ciag liczb ktory podales to: {ciag}')
print("awers: ", awers)
print(f'rewers: {rewers}')





