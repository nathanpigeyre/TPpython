print("donne un chiffre entre 0 et 20")
vmin = 0
vmoy = 0
vmax = 0
x=0
n = 0
while n!=10:
    if 0 < x < 20 or 0 == x or x == 20:
        x = float(input("File un nombre:"))
        if x <10:
            vmin = vmin + 1
            n = n + 1
        elif 10<x<15 or x==10:
            vmoy = vmoy + 1
            n = n + 1
        else:
            vmax = vmax + 1
            n = n + 1
    else:
        x = float(input("File un autre nombre:"))

print("Le nombre de valeurs inférieur strictement à 10 est :{}".format(vmin))
print("Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est :{}".format(vmoy))
print("Le nombre de valeurs supérieur ou égale à 15est :{}".format(vmax))




