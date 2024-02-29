numero1=int(input("Dime la distancia a recorrer: "))
numero2=int(input("Dime el/los dia/s de estancia/s: "))
if numero1>800 and numero2 > 7:
    xd=numero1*2.5
    xd2=(xd*30)/100
    print("El precio del billete es ",xd2)
else:
    xd=numero1*2.5
    print("El precio del billete es ",xd)