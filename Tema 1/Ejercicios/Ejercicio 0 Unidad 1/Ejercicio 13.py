segundos=int(input("Dime un tiempo en segundos: "))
operacion=int(segundos/3600)
resto=int(segundos%3600)
operacion2=int(resto/60)
resto2=int(operacion2%60)
print("Horas " + str(operacion) , "Minutos " + str(operacion2), "Segundos " + str(resto2))


