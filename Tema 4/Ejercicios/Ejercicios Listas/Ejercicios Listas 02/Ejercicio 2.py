cuenta=int(input("Dime cuantos valores quieres introducir: "))
cuen=0
lista=[]
while cuen < cuenta:
    cuen+=1
    if cuen > 0:
        palabra=input("Dime la palabra: ")
        lista.clear()
        lista.append(palabra)
    print("yo estudio",lista)