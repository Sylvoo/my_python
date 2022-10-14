k = int(input("kazik: "))
t = int(input("trener: "))
m = int(input("guz: "))

if k<t:
    i = 0
    while k<t:
        k = k+m
        i += 1
print(k)
print(i)