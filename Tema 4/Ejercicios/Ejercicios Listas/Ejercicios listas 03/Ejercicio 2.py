#lista=[]
#for x in range(1,6):
    #palabra = input("Dime una palabra: ")
    #lista.append(palabra)
    #reversed(lista)
#lista2 = list(lista.__reversed__())
#print(lista2)

lista = []
for x in range(1,6):
    palabra = int(input("Dime tu nota "))
    lista.append(palabra)
maxima = max(lista)
print("La nota maxima es", maxima)
minima = min(lista)
print("La nota minima es", minima)
media = ((lista))/5
print("La media es", media)


