nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
sum = 0.0

notes = [0] * nombreEtudiants

for i in range(nombreEtudiants):
    notes[i] = float(input(f"Note étudiant {i+1} : "))
    sum = sum + notes[i]

mean = sum / nombreEtudiants
print(f"Moyenne de la classe : {mean}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    gap = notes[i] - mean
    print(f"{i+1} | {notes[i]} | {gap}")