numero1=int(input("Dime las horas trabajadas: "))
numero2=input("Dime la jornada en la que trabajas: ")
numero3=(input("Dime que dia trabajas: "))
if numero3=="domingo":
    if numero2=="diurno":
        xd=numero1*30
        print("Cobraras ",xd)
    if numero2=="nocturno":
        xd=numero1*45
        print("Cobraras ",xd)
else:
    if numero2=="diurno":
        xd=numero1*20
        print("Cobraras ",xd)
    if numero2=="nocturno":
        xd=numero1*35
        print("Cobraras ",xd)