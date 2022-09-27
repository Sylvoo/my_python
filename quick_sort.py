tab = [5, 6, 30, 15, 44, 33, 98]

def quicksort(tab):
    pivot = tab[len(tab) // 2]
    sort = []
    for i in range(0,7):
        if tab[i] < pivot:
            sort.append(tab[i])
        elif tab[i] >= pivot:
            sort.append(pivot)
            pivot = tab[i
        print(sort)
    print(sort)

quicksort(tab)