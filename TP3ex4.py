m = input("tu veut choisir quelle boucle :")
n = int(input("donne une valeur :"))
if m =="for":
    x = 1
    for i in range(1, n+1):
        x = x * i
        print(x)
    print("Donc = {}".format(x))
elif m == "while":
    x = 1
    while (n > 1):
        x *= n
        n -= 1
        print(x)
    print("Donc = {}".format(x))
else:
    print("tu t'es trompé de mot")