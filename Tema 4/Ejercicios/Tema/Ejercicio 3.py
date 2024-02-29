lista=[1,25,12,4,8,5,93,4]
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i]< lista[j]:
            resultado=lista[i]
            lista[i]=lista[j]
            lista[j]=resultado
print(lista)

lista.sort()
print(lista)

