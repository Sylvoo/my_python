
x, y, z = map(int, input().split())

if x+y > z and x+z > y and z+y > x:
    print("yes")
else:
    print("No")


