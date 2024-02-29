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
    susti=input("Dime la palabra a borrar: ")
    xd3=lista.count(susti)
    if xd3 == 0:
        print("no aparece")
    else:
        for x in range(xd3):
            cuenta=lista.remove(susti)
        print(lista)