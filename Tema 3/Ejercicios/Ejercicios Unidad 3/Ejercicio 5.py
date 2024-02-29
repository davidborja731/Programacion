while True:
    nombre=input("Dime tu nombre ")
    if nombre.istitle():
        print("Has introducido correctamente tu nombre ",nombre)
    else:
        print("El nombre no está en formato título")

