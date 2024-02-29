numero = int(input("Dime un numero: "))
lista = [numero]
if lista == 2:
    print("Tiene 28 dias")
elif lista == 4 or 6 or 9 or 11:
    print("Tiene 30 dias")
elif lista == 1 or 2 or 3 or 5 or 7 or 8 or 10 or 12:
    print("Tiene 31 dias")
elif lista > 12:
    print("Imposible")