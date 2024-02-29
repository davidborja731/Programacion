numero=int(input("Dime un numero: "))
def xd(numero):
    numero1= 0
    numero2= 1
    for i in range(numero):
        if numero1 <= i:
            print(numero1)
            numero1, numero2 =numero2, numero1 + numero2
xd(numero)