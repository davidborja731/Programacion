lista=[]
for x in range(1,6):
    numero=int(input("Dime tu nota: "))
    lista.append(numero)
print(lista)
lista2=[]
for j in range(1,6):
    numero1=int(input("Dime tu nota: "))
    lista2.append(numero1)
print(lista2)
lista3=[lista+lista2]
print(lista3)

