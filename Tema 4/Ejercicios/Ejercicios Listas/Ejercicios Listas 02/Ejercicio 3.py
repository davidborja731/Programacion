cuenta=int(input("Dime cuantos valores quieres introducir: "))
cuen=0
lista=[]
while cuen < cuenta:
    cuen+=1
    if cuen > 0:
        palabra=input("Dime la asignatura: ")
        nota=input("Dime tu nota: ")
        lista2=[nota]
        lista.clear()
        lista.append(palabra)
    print("En",lista,"Tengo un",lista2)