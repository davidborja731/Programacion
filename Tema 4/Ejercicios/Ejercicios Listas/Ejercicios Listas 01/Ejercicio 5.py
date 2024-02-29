cuenta=int(input("Dime cuantos valores quieres introducir: "))
xd=0
lista=[]
while xd < cuenta:
    xd+=1
    if xd > 0:
        palabra=input("Dime la palabra: ")
        lista.append(palabra)
print(lista)
cuenta2=int(input("Dime cuantos valores quieres introducir: "))
xd2=0
lista1=[]
while xd2 < cuenta2:
    xd2+=1
    if xd2 > 0:
        palabra2=input("Dime la palabra: ")
        lista1.append(palabra2)
print(lista1)
lista3=[]
for i in lista:
    if not i in lista1:
        lista3.append(i)
for i in lista1:
    if not i in lista:
        lista3.append(i)
print(lista3)
