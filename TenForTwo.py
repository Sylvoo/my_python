# Zamiana z liczby dziesietnej na liczbe binarna 
def TenForTwo(liczba):
    tab = []
    while liczba > 1:
        wynik = liczba % 2
        tab.append(wynik)
        liczba = liczba / 2
        if liczba == 1: return 1
    for i in tab:
        print (i)
    
        
print(TenForTwo(5))

# Nie do konca dziala tak jak chcemy 
# Pokazuje liczby we float 
        

