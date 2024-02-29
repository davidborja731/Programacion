import random
intentos=0
numero=random.randint(1,100)
print("Estoy pensdando un numero entre el 1 y el 100")
while intentos < 5:
    adivina=int(input("Dime un numero: "))
    intentos+=1
    if adivina < numero:
        print("El numero es muy bajo")
    elif adivina > numero:
        print("El numero es muy alto")
    elif adivina == numero:
        print("Has acertado el numero ",numero," en",intentos," intentos" )
        respuesta=input("¿Quieres continuar? ")
        break
    if intentos >= 5:
        break
