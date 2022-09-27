
tab = []
for i in range (6):
    x = int(input("Podaj liczbe: "))
    tab.append(x)

def mergeSort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        l = tab[:mid]
        r = tab[mid:]
        print("l: ", l); print("r: ", r)
        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                tab[k] = l[i]
                i += 1
            else:
                tab[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            tab[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            tab[k] = r[j]
            j += 1
            k += 1
        print("_PO: ", tab)

mergeSort(tab)
print(tab)








