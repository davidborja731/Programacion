# ponemos que pregunta es igual a si para que el while(bucle) pueda iniciar
pregunta = "si"
# .lower() transforma el texto a minusculas y .upper() transforma el texto a mayusculas
while pregunta.lower() == "si":
    # pedimos al usuario los dos numeros que el programa usara para calcular
    numero = int(input("dime un numero: "))
    numero1 = int(input("Dime oro numero: "))
    # con int o float transformamos el input que por defecto es texto plano a un numero
    xd = float(numero)
    xd1 = float(numero1)
    # preguntamos al usuario que operacion quiere hacer 
    opcion = input("que quieres hacer elige entre suma, resta, multiplicacion y division: ")
    # con if inidicamos que si opcion es igual(==) o diferente(!=) a una de las opciones que damos haga una funcion o otra 
    # la estructura del if es poner if en caso de que se cumpla y else en caso de que no se cumpla
    if opcion == "suma":
        resultado = xd + xd1
    elif opcion == "resta":
        resultado = xd - xd1
    elif opcion == "multiplicacion":
        resultado = xd * xd1
    elif opcion == "division":
        # para la division indicamos que en caso de que el dividendo sea 0 indicaremos un mensaje de error
        if xd1 != 0:
            resultado = xd / xd1
        else:
            resultado = "no se puede dividir por cero"
    # en caso de que el usuario no eliga uan de las opciones que se le dan lanzamos un mensaje que le avisara
    else:
        resultado = "no se bro elige una de las 4 opciones"
    print("el resultado es", resultado)
    # con esto preguntamos si el usuario quiere seguir haciendo operaciones y en caso de contestar que si el bucle se inciara 
    pregunta = input("quieres hacer otra operacion contesta si o no : ")








    
