import random
cuenta=0
lista=[]
while cuenta <= 10:
    cuenta+=1
    aleatorio=random.randint(1,10)
    lista.append(aleatorio)
    ale=aleatorio
    lista.append(ale**ale)
    alea=aleatorio
    lista.append(alea**3)
print(lista)
    