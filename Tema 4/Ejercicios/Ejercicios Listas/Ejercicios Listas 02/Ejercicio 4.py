cuenta=6
cuen=0
lista=[]
while cuen < cuenta:
    cuen+=1
    if cuen > 0:
        palabra=int(input("Introduce el numero ganador: "))
        lista.append(palabra)
ordenado=sorted(lista)
print(ordenado)