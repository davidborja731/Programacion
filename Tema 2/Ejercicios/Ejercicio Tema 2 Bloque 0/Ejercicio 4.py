xd=input("(1)Piedra, (2)papel o (3)Tijera: ")
xd2=input("(1)Piedra, (2)papel o (3)Tijera: ")
if xd == "Piedra" or 1 and xd2== "Tijera" or 3:
    print("Gana el jugador 1")
elif xd2 == "Piedra" or 1 and xd== "Tijera" or 2:
    print("Gana el jugador 2")
elif xd2 == "Papel" or 2 and xd== "Tijera" or 3:
    print("Gana el jugador 1")
elif xd == "Papel" or 2 and xd2== "Tijera" or 3:
    print("Gana el jugador 2")
elif xd2 == "Papel" or 2 and xd== "Piedra" or 1:
    print("Gana el jugador 2")
elif xd2 == "Piedra" or 1 and xd== "Papel" or 2:
    print("Gana el jugador 2")