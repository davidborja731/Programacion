super=int(input("Dime un mes por numero: "))
super1=int(input("Dime un año: "))
if super1%4 == 0:
    if super1%100:
        if super1%400:
            bisiesto=True
else:
    bisiesto=False
if bisiesto==True and super <=12:
    if super==[9,4,6,11]:
        print("Este mes tiene 30 dias")
    elif super==2:
        print("Febrero tiene 29 dias")
    else:
        print("Este mes tiene 31 Dias")
else:
     print("El año solo tiene doce meses")
if bisiesto==False and super <=12:
    if super==[9,4,6,11]:
        print("Este mes tiene 30 dias")
    elif super==2:
        print("Febrero tiene 28 dias")
    else:
        print("Este mes tiene 31 Dias")
else:
    print("El año solo tiene doce meses")
        


