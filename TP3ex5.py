T=0
Y=0
while T == 0:
    hd = int(input("Donnez l’heure de début de la location (un entier) : "))
    hf = int(input("Donnez l’heure de fin de la location (un entier) : "))
    if hd ==hf :
        print("Attention ! l’heure de fin est identique à l’heure de début.")
    elif hd > hf :
        print("Attention ! le début de la location est après la fin ...")
    elif hd >24 or hf >24:
        print("Les heures doivent être comprises entre 0 et 24 !")
    elif hd<0 or hf<0:
        print("Erreur!!!!!!!!")
    else :
        T = 1
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
s=0
f=0
g=0
c=0
if 0<= hd <=6 and 1<=hf<=7:
    s1= hf - hd
    print("{} heure(s) au tarif de 1.0 euro(s)".format(s1))
elif 17<=hd<=23 and 18<=hf<=24:
    s2= hf - hd
    print("{} heure(s) au tarif de 1.0 euro(s)".format(s2))
elif 7<=hd<=16  and 8<=hf<=17:
    s3= 2*(hf - hd)
    v=(hf - hd)
    print("{} heure(s) au tarif de 2.0 euro(s)".format(v))
elif 0<=hd<=6 and 8<=hf<=17:
    f= 8-hd
    g= hf - 8
    s4=2*g+f
    print("{} heure(s) au tarif de 1.0 euro(s)".format(f))
    print("{} heure(s) au tarif de 2.0 euro(s)".format(g))
elif 0<=hd<=6 and 18<=hf<=24:
    c= 7-hd
    g= 10
    f=c+(hf-17)
    s5=2*g+f
    print("{} heure(s) au tarif de 1.0 euro(s)".format(f))
    print("{} heure(s) au tarif de 2.0 euro(s)".format(g))
elif 7<=hd<=16 and 17<=hf<=24:
    g=17-hd
    f=hf - 17
    print("{} heure(s) au tarif de 1.0 euro(s)".format(f))
    print("{} heure(s) au tarif de 2.0 euro(s)".format(g))
    s6=2*g+f
s=s1+s2+s3+s4+s5+s6
print("Le montant total à payer est de {}.0 euro(s).".format(s))
