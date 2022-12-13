L1 = [2, 7, 5, 6, 6, 1, 7, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
b = 0
for i in L1:
    T = L1.count(i)
    if T > b:
        b = T
        h = i
print("\nLe nombre le plus frequent dans la liste est le :{} ({} x)".format(h, b))


""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""