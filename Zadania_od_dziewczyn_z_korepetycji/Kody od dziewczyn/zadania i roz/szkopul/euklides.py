# a,b = map(int,input().split())
#
# while a!=b:
#     if a>b:
#         a = a-b
#     else:
#         b = b-a
# print(a)

a,b = map(int,input().split())

while b!=0:
    r = a%b
    a = b
    b = r
print(a)