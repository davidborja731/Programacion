palabras = int(input("Cuantas palabras quieres escribir? "))
cuenta = 0
lista = []
while cuenta != palabras:
    cuenta += 1
    palabra = input("Dime la palabra a introducir ")
    lista.append(palabra)
print(lista)
palabras2 = int(input("Cuantas palabras quieres escribir? "))
cuenta2 = 0
lista2 = []
while cuenta2 != palabras2:
    cuenta2 += 1
    palabra2 = input("Dime la palabra a introducir ")
    lista2.append(palabra2)
print(lista2)
#for i in lista:
    #if i in lista2:
        #lista.remove(i)
#print(lista)
lista3=[]
for i in lista:
    if i in lista2:
        lista3.append(i)
for i in lista2:
    if i in lista:
        lista3.append(i)
for i in lista3:
    comprobar=lista3.count(i)
    if comprobar > 1:
        lista3.remove(i)
print("Lista de palabras comunes sin repetir",lista3)
lista4=[]
for i in lista:
    if i not in lista2:
        lista4.append(i)
print("Lista de palabras que solo aparecen en lista1",lista4)
lista5=[]
for i in lista2:
    if i not in lista:
        lista5.append(i)
print("Lista de palabras que solo aparecen en lista1",lista5)
lista6=[]
for i in lista:
    for x in lista2:
        if i in lista2 and x in lista:
            lista6.append(x)
            testeo = lista6.count(i)
            testeo2 = lista6.count(x)
            if testeo > 1:
                lista6.remove(i)
print("Lista de palabras que se encuentran en ambas listas",lista6)
