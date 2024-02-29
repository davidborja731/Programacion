numero=float(input("Dime un numero: "))
def signo(numero):
    if numero < 0:
        print("-1")
    elif numero > 0:
        print("1")
    else:
        print("0")
signo(numero)