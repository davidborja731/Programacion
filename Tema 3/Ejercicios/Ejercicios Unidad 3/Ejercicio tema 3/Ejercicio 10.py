import random
intentos=0
numero=random.randint(1,100)
print("Estoy pensdando un numero entre el 1 y el 100")
while True:
    adivina=float(input("Dime un numero: "))
    intentos=intentos+1
    if adivina < numero:
        print("El numero es muy bajo")
    if adivina > numero:
        print("El numero es muy alto")
    if adivina == numero:
        print("Has acertado el numero ",numero," en",intentos," intentos" )
        
