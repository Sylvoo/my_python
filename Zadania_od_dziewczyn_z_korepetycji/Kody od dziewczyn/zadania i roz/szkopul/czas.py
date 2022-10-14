t = int(input("sekundy: "))

if t > 0:
    g = t // 3600
    min = (t - g*3600) // 60
    s = t - g*3600 - min*60
    print(g,"h",min,"min",s,"s")
else:
    print("blad")