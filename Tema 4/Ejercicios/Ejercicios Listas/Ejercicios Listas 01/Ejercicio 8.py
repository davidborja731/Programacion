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
    if i in lista1:
        lista3.append(i)
print("Las palabras en comun son:",lista3)
lista4=[]
for i in lista:
    if not i in lista1:
        lista4.append(i)
print("Las palabras que aparecen solo en la lista numero 1 son:",lista4)
lista5=[]
for i in lista1:
    if not i in lista:
        lista5.append(i)
print("Las palabras que aparecen solo en la lista numero 2 son:",lista5)
print("Todas las palabras son",lista+lista1)