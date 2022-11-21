n = int(input("Podaj ktory wyraz ciagu(1 to min) : "))

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        wynik = fib(x-1) + fib(x-2)
        return wynik

print(fib(n))