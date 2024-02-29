numero1=int(input("Dame un numero: "))
numero2=int(input("Dame un numero: "))
numero3=int(input("Dame un numero: "))
xd=min(numero1,numero2,numero3)
xd2=max(numero1,numero2,numero3)
if xd==numero1 and xd2==numero2:
    print("El numero minimo es ",xd," El numero maximo es ",xd2,"El numero mediano es el ",numero3)
elif xd==numero2 and xd2==numero1:
    print("El numero minimo es ",xd," El numero maximo es ",xd2,"El numero mediano es el ",numero3)
elif xd==numero1 and xd2==numero3:
    print("El numero minimo es ",xd," El numero maximo es ",xd2,"El numero mediano es el ",numero2)
elif xd==numero3 and xd2==numero1:
    print("El numero minimo es ",xd," El numero maximo es ",xd2,"El numero mediano es el ",numero2)
elif xd==numero2 and xd2==numero3:
    print("El numero minimo es ",xd," El numero maximo es ",xd2,"El numero mediano es el ",numero1)
elif xd==numero3 and xd2==numero2:
    print("El numero minimo es ",xd," El numero maximo es ",xd2,"El numero mediano es el ",numero1)

