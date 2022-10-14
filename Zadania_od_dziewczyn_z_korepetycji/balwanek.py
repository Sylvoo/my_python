# x litry sniegu pierwsza kula
# k listry sniegu druga kula

x = 10
k = 2

balwan1 = (k + k*2 + k*4) * 1000
balwan2 = (k/2 + k + k*2) * 1000
balwan3 = (k/4 + k/2 + k) * 1000

if balwan1 < (x * 1000):
    print(balwan1)
elif balwan2 < (x * 1000) and balwan2 > balwan3:
        print(balwan2)
else:
    print(balwan3)

if balwan2 < (x * 1000) and balwan2 > balwan3:
    print("true")
else:
    print("false")

