
tab = [20, 1, 3, 5, 8, 11, 23]
print(tab)
def quicksort(tab):
    if len(tab) > 1:
        lower = []
        equal = []
        higher = []
        pivot = tab[0]
        for x in tab:
            if pivot > x:
                lower.append(x)
            elif pivot < x:
                higher.append(x)
            else:
                equal.append(x)
        return quicksort(lower) + equal + quicksort(higher)
    else:
        return tab


print(quicksort(tab))
