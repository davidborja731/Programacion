cuenta=0
lista=[]
while cuenta < 5:
    cuenta+=1
    temperaturamax=int(input("Dime la temperatura maxima: "))
    lista.append(temperaturamax)
    temperaturamin=int(input("Dime la temperatura mimima: "))
    lista.append(temperaturamin)
print("Dia 1 maxima:",lista[0])
print("Dia 1 minima:",lista[1])
print("Dia 2 maxima:",lista[2])
print("Dia 2 minima:",lista[3])
print("Dia 3 maxima:",lista[4])
print("Dia 3 minima:",lista[5])
print("Dia 4 maxima:",lista[6])
print("Dia 4 minima:",lista[7])
print("Dia 5 maxima:",lista[8])
print("Dia 5 minima:",lista[9])
print("Dia 1 Temperatura media:",str((lista[0]+lista[1])/2))
print("Dia 2 Temperatura media:",str((lista[2]+lista[3])/2))
print("Dia 3 Temperatura media:",str((lista[4]+lista[5])/2))
print("Dia 4 Temperatura media:",str((lista[6]+lista[7])/2))
print("Dia 5 Temperatura media:",str((lista[8]+lista[9])/2))