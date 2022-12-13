L1 = [2, 7, 5, 6, 6, 1, 7, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
y = 0
h = 0
b = 0
T = [0] * len(L1)
for i in range(len(L1)):
    for j in L1:
        if L1[i] == j:
            T[i] = T[i] + 1
for u in range(len(T)):
    if T[u] > y:
        y = T[u]
for w in range(len(T)):
    if T[w] == y:
        b = T[w]
        h = L1[w]
        break
print("\nLe nombre le plus frequent dans la liste est le :{} ({} x)".format(h, b))


""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""