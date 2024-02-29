lista=[]
cuenta=1
while cuenta > 0:
    numero=int(input("Dime un numero: "))
    if numero > 0:
        lista.append(numero)
    else:
        break
print(lista)
