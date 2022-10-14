a1,b1 = map(int,input().split("/"))
a2,b2 = map(int,input().split("/"))

#czemu przy tym wyskakuje mi
#invalid literal for int() with base 10:
#jak wpisuje liczby

x = b1
y = b2
while b1!=b2:
    if b1 > b2:
        b2 += y
    else:
        b1 += x
print(b1)