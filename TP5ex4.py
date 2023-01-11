somme = int(input("Saisissez une somme d'argent en euros : "))
nb_100 = somme // 100
somme = somme % 100
nb_50 = somme // 50
somme = somme % 50
nb_10 = somme // 10
somme = somme % 10
nb_2 = somme // 2
nb_1 = somme % 2
print("c'est donc {} billets de 100, {} de 50, {} de 10, {} pièces de 2 et {} pièce 1.".format(nb_100, nb_50, nb_10, nb_2, nb_1))
