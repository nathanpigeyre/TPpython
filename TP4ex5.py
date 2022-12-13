while True:
    date = input("entrz la date sous la forme jjmmaaaa :")
    j= int(date[0] + date[1])
    m= int(date[2] + date[3])

    a = str()
    for i in range(4, len(date)):
        a = a + date[i]
    a = int(a)

    if m == 2:
        if (j > 28) & ((a % 4) !=0) or ((a % 100) != 0) or ((a % 400) != 0):
            print(f"La date est fausse, il n'y a que 28j dans le mois de février de l'année {a}")
        elif j > 29:
            print(f"La date est fausse, il n'y a que 29j dans le mois de février de l'année {a}")
        else:
            print(f"La date {j}/{m}/{a} est correcte")
            break
    elif (m > 12) or (j > 31):
        print("La date est fausse, un mois ne peut contenir plus que 31j")
    elif (1 <= m <= 7) & (m % 2 == 0) & (j > 30):
        print("La date est fausse, il n'y a que 30j dans le mois indiqué")
    elif (8 <= m <= 12) & (m % 2 != 0) & (j > 30):
        print("La date est fausse, il n'y a que 30j dans le mois indiqué")
    else:
        print(f"La date {j}/{m}/{a} est correcte")
        break