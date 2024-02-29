numero1=1
creciente=True
while numero1 != -1 and creciente==True:
    numero1=int(input("Dime un numero: "))
    if numero1 > numero1:
        creciente=True
        print(numero1)
    elif numero1 < numero1:
        print("La cadena no es creciente")
        creciente=False