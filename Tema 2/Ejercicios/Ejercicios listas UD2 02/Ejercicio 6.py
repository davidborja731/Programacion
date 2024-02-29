numero1=1
pares=0
impares=0
while numero1 != -1:
    numero1=int(input("Dime un numero: "))
    if numero1==1:
        impares+=1
    elif numero1%2==0:
        pares+=1
    else:
        impares+=1
print("Hay un total de",pares,"numeros pares")
print("Hay un total de",impares,"numeros impares")
