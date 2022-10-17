# CHOINKA

'''
    *
   ***
  *****
 *******
    *
   ***
  *****
 *******
*********
'''

gwiazdka = 1
spacja = 4

for i in range(4):
    while spacja >= 1:
        print(spacja * " ", gwiazdka * "*")
        spacja -= 1
        gwiazdka += 2

if spacja == 0:
    gwiazdka = 1
    spacja = 4

for i in range(4):
    while spacja >= 0:
        print(spacja * " ", gwiazdka * "*")
        spacja -= 1
        gwiazdka += 2





