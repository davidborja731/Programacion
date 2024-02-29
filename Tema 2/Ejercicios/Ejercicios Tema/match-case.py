pregunta="si"
while pregunta=="si":
    pregunta1=int(input("Dame un numero: "))
    pregunta2=int(input("Dame otro numero: "))
    pregunta3=input("¿que operacion quieres hacer? ")
    match pregunta3:
        case "suma":
            suma=pregunta1+pregunta2
            print( pregunta1,"+",pregunta2,"=",suma )
        case "resta":
            resta=pregunta1-pregunta2
            print( pregunta1,"-",pregunta2,"=",resta)
        case "multiplicacion":
            multiplicacion=pregunta1*pregunta2
            print( pregunta1,"*",pregunta2,"=",multiplicacion)
        case "division":
            division=pregunta1/pregunta2
            print( pregunta1,"/",pregunta2,"=",division)
        case _:
            print("Operacion desconocida")
    pregunta=input("¿Quieres hacer otra operacion? ")