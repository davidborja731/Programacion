lista=[]
for x in range(1,6):
    palabra=float(input("Dime tu nota: "))
    lista.append(palabra)
print("El minimo es",min(lista))
print("El maximo es",max(lista))
media=sum(lista)/len(lista)
print("La media es",media)
