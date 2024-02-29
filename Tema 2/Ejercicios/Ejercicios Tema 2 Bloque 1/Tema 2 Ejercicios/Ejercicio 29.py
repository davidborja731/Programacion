respuesta="si"
while respuesta=="si":
    nota=float(input("Dime la nota: "))
    if nota >= 0 and nota < 5:
        print("el alumno esta suspenso")
    elif nota > 5 and nota <= 6:
        print("el alumno esta aprobado")
    elif nota> 6 and nota < 7:
        print("el alumno tiene un bien")
    elif nota>=7 and nota<=8:
        print("el alumno tiene un notable")
    elif nota> 8 and nota<=10:
        print("el alumno tiene un sobresaliente")
    elif nota <0:
        print("Has introducido un numero negativo")
        exit()
    elif nota >10:
        print("Has introducido un numero supeior a 10")
        exit()
    respuesta=input("¿Quieres seguir introduciendo notas?(si/no) ")