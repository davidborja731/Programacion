numero1=int(input("Dime un numero: "))
numero2=int(input("Dime un numero: "))
numero3=int(input("Dime un numero: "))
if numero1 < numero2 and numero2 < numero3:
    print("El menor es el numero", numero1)
if numero2 < numero1 and numero2 < numero3:
    print("El menor es el numero", numero2)
if numero3 < numero2 and numero3 < numero1:
    print("El menor es el numero", numero3)   