S1 = []
S1 = str(input('Veuillez entrer la note du module 1 et le coefficient correspondant : '))
S2 = S1.split(" ")
S3 = S2[0]
S4 = S2[1]
S3 = float(S3)
S4 = float(S4)
note = S3 * S4
A1 =[]
A1 = str(input('Veuillez entrer la note du module 2 et le coefficient correspondant : '))
A2 = A1.split(" ")
A3 = A2[0]
A4 = A2[1]
A3 = float(A3)
A4 = float(A4)
note = note + (A3* A4)
B1 =[]
B1 = str(input('Veuillez entrer la note du module 3 et le coefficient correspondant : '))
B2 = B1.split(" ")
B3 = B2[0]
B4 = B2[1]
B3 = float(B3)
B4 = float(B4)
note = note + (B3* B4)
C1 =[]
C1 = str(input('Veuillez entrer la note du module 4 et le coefficient correspondant : '))
C2 = C1.split(" ")
C3 = C2[0]
C4 = C2[1]
C3 = float(C3)
C4 = float(C4)
note = note + (C3* C4)
D1 =[]
D1 = str(input('Veuillez entrer la note du module 5 et le coefficient correspondant : '))
D2 = D1.split(" ")
D3 = D2[0]
D4 = D2[1]
D3 = float(D3)
D4 = float(D4)
note = note + (D3* D4)
result = note / (S4 + A4 + B4 + C4 +D4)
print("votre moyenne générale est a :", round(result,2))
if result >= 10 and S3 >= 8 and A3 >= 8 and B3 >= 8 and C3 >= 8 and D3 >= 8:
    print('Vous êtes admis !')
else :
    print("Vous n'êtes pas admis car vos notes ne sont pas suffisante")
