x = int(input("x: "))
y = int(input("y: "))

if x > 0:
    if y > 0:
        print("ćw 1")
    elif y < 0:
        print("ćw 2")
    else:
        print("os x")
elif x < 0:
    if y > 0:
        print("ćw 4")
    elif y < 0:
        print("ćw 3")
    else:
        print("os x")
else:
    print("os y")