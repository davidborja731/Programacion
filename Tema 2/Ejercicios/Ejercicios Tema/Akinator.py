respuesta="si"
while respuesta =="si":
    pregunta1=input("Tu personaje puede volar ")
    pregunta2=input("Tu personaje Es humano ")
    pregunta3=input("Tu personaje tiene mascara ")
    if pregunta1 == "si":
        if pregunta2=="si":
            if pregunta3=="si":
                print("Iron Man")
            else:
                print("Capitana Marvel")
        if pregunta2=="no":
            if pregunta3=="si":
                print("Ronan el acusador")
            else:
                print("Vision")
    if pregunta1 == "no":
        if pregunta2=="si":
            if pregunta3=="si":
                print("Spiderman")
            else:
                print("Hulk")
        if pregunta2=="no":
            if pregunta3=="si":
                print("Black Boltr")
            else:
                print("Thanos")
    respuesta=input("¿Quieres que adivine otro personaje?: ")
       
