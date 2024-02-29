numero1=int(input("Dime un numero: "))
lista=[]
for i in range(1,numero1+1):
    if i%2==0 or i%3==0:
        lista.append(i)
print(lista)


