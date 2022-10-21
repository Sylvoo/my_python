a = int(input())
b = int(input())

def nwd(a,b):
    while b >= 0:
        if b == 0:
            print(a)
            break
        else:
            r = a % b
            a = b
            b = r


nwd(a,b)