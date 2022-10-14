n = int(input("n: "))
awers = 0
rewers = 0
for i in range(n):
    x = int(input("-"))
    if x ==0:
        awers += 1
    elif x == 1:
        rewers += 1
print("awers: ", awers)
print("rewers: ", rewers)