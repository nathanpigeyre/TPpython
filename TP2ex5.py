
x = int(input("Entrez un nombre entier:"))
if x == 0:
    print("Le nombre est zéro (et il est pair)")
elif x > 0:
    x = x % 2
    if x == 0:
        print("Le nombre est positif et paire")
    else:
        print("Le nombre est positif et impair")
else:
    x = x % 2
    if x == 0:
        print("Le nombre est négatif et paire")
    else:
        print("Le nombre est négatif et impair")

