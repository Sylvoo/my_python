
'''
x = l śniegu
k = kula kasi z k litrów śniegu
3 kule jedna od drugiej o 2x mniejsza
'''

k = int(input("litry sniegu: "))
x = int(input("kula kasi: "))

if k > x:
    najw1 = x/2 + x + 2*x
    najw2 = x + 2*x + 4*x
    najw3 = x/4 + x/2 + x
    if najw2 > k:
        if najw1>k:
            print(int(najw3) * 1000)
        else:
            print(int(najw1) * 1000)
    else:
        print(int(najw2) * 1000)
else:
    print("za malo sniegu")