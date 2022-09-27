tab = [5, 6, 30, 15, 44, 33, 98]

def quicksort(tab):
    pivot = tab[len(tab) // 2]
    sorted = []
    for i in range(0,7):
        if tab[i] < pivot:
            sorted.append(tab[i])
            i+=1
        elif tab[i] == pivot:
            sorted.append(tab[i])
            i+=1
        elif tab[i] > pivot:
            sorted.append(pivot)
            pivot = tab[i]
            i+=1
        print(sorted)
    print(sorted)

quicksort(tab)