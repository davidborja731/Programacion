cuenta=int(input("Dime cuantos valores quieres introducir: "))
xd=0
lista=[]
while xd < cuenta:
    xd+=1
    if xd > 0:
        palabra=input("Yo estudio ")

        lista.append(palabra)
print("yo estudio",lista)
