import random
x = random.randint(0,100)
n=0
m=0
print("Devine mon nombre il est compris entre 0 et 100\n")
while n != x:
    n=int(input("propose un nombre :"))
    m=m+1
    if n > x:
        print("ma valeur est plus petite")
    elif n < x:
        print("ma valeur est plus grande")
    else:
        break
print("En effet mon nombre est bien {}".format(x))
print("Tu l'as trouvé en {} essaie(s)".format(m))

