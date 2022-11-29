BASE = 4
fromage = 800.0
fromage = int(fromage)/4
eau = 2
eau = int(eau)/4
ail = 2
ail = int(ail)/4
pain = 400
pain = int(pain)/4
BASE=input("Entrez le nombre de personne(s) conviées à la fondue :")
print("Pour faire une fondue fribourgeoise pour {} personnes, il vous faut :".format(BASE))
fromage = int(BASE)*fromage
eau = int(BASE)*eau
ail = int(BASE)*ail
pain = int(BASE)*pain
print("{} gr de fromage".format(fromage))
print("{} dl d'eau".format(eau))
print("{} gousse(s) d'ail".format(ail))
print("{} gr de pain".format(pain))