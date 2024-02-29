cuenta=int(input("Dime cuantos valores quieres introducir: "))
xd=0
lista=[]
while xd < cuenta:
    xd+=1
    if xd > 0:
        palabra=input("Dime la palabra: ")
        lista.append(palabra)
print(lista)
lista2=lista
print(lista2[::-1])