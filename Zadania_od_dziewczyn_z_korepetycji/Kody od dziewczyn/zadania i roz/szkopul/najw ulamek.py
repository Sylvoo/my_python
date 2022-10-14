a1 = int(input("a1: "))
a2 = int(input("a2: "))
b1 = int(input("b1: "))
b2 = int(input("b2: "))
c1 = int(input("c1: "))
c2 = int(input("c2: "))

a = b2 * c2 * a1
b = a2 * c2 * b1
c = a2 * b2 * c1

tab=[a,b,c]
if max(tab) == a:
    print(a1,a2)
elif max(tab) == b:
    print(b1,b2)
elif max(tab) == c:
    print(c1,c2)
