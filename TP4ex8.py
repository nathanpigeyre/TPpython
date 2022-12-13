dic = {"name": "toto", "firstname": "titi", "promo": 2022, "group": 202}
dic2 = {"name": "tata", "firstname": "tutu", "promo": 2022, "group": 102}
binôme = {'1': dic, '2': dic2}
print("Les étudiants formants le binôme sont :")
for key in binôme.keys():
    print("- L'étudiant {} {} du groupe {}".format(binôme[key]["name"], binôme[key]["firstname"], binôme[key]["group"]))
