cuenta=int(input("Dime cuantos valores quieres introducir: "))
xd=0
lista=[]
while xd < cuenta:
    xd+=1
    if xd > 0:
        palabra=input("Dime la palabra: ")
        lista.append(palabra)
if cuenta==0:
    print("Imposible")
else:
    susti=input("Dime la palabra a sustituir: ")
    xd3=lista.count(susti)
    if xd3 == 0:
        print("no aparece")
    else:
        susti2=input("Dime la palabra que la sustituira: ")
        cuenta=lista.count(susti)
        for x in range(cuenta):
            xd4=lista.index(susti)
            lista[xd4]=susti2
        print(lista)

    