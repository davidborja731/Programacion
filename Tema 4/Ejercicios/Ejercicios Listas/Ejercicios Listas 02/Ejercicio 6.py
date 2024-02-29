cuenta=6
cuen=0
lista=[]
while cuen < cuenta:
    cuen+=1
    if cuen > 0:
        palabra=input("Dime la asignatura: ")
        nota=int(input("Dime tu nota: "))
        lista.append(nota)
        lista.append(palabra)
    if nota < 5:
        print("Repite",palabra)
print(lista)