numero=int(input("Dame un numero: "))
def suma(numero):
    if numero ==1:
        return 1
    else:
        numero+= suma(numero-1)
        return numero
print(suma(numero))