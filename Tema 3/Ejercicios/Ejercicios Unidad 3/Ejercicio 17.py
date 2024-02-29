num1=float(input("Dime la nota del examen "))
def nota(num1):
    if num1<0:
        print("No puedes sacar un numero negativo")
    elif num1<5:
        print("Estas suspenso")
    elif num1<7:
        print("Aprobado")
    elif num1<9:
        print("Notable")
    elif num1<=10:
        print("Sobresaliente")
    else:
        print("No puedes sacar mas de un diez")
nota(num1)
