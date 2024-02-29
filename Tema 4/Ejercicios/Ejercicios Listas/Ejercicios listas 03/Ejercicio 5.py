import random
cuenta=0
lista=[]
while cuenta <= 9:
    cuenta+=1
    aleatorio=random.randint(1,10)
    lista.append(aleatorio)
lista.sort()
print(lista)