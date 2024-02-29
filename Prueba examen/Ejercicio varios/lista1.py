palabras = int(input("Cuantas palabras quieres escribir? "))
cuenta = 0
lista = []
while cuenta != palabras:
    cuenta += 1
    palabra = input("Dime la palabra a introducir ")
    lista.append(palabra)
print(lista)

#buscar = input("Dime que palabra quieres que busque ")
#print("la palabra aparece", lista.count(buscar),"vez/veces")
#palabra1 = input("Introduce la palabra a sustituir: ")
#palabra2 = input("Introduce la palabra que la va a sustituir: ")
#for i in range(len(lista)):
    #if lista[i] == palabra1:
        #lista[i] = palabra2
#print(lista)

#borrar = input("Dime la palabra a borrar ")
#if borrar in lista:
    #todo = lista.count(borrar)
    #seguro = 0
    #while seguro != todo:
        #seguro += 1
        #lista.remove(borrar)
    #print(lista)
#else:
    #print("La palabra a borrar no esta en la lista")
#lista2=lista
#print(lista2[::-2])

#for i in lista:
    #comprobacion = lista.count(i)
    #if comprobacion > 1:
        #lista.remove(i)
#print(lista)
