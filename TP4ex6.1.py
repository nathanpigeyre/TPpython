tab = [5, 2, 4, 8, 1, 3]
print(tab)
for i in range(len(tab)-1):
    min = tab[i]
    for j in range(i, len(tab)):
        if tab[j] < min:
            min = tab[j]
            x = j
    if min < tab[i]:
        t = tab[i]
        tab[i] = tab[x]
        tab[x] = t
    print(tab)