contador=0
for i in range(15):
    import random
    var="1","x","2"
    xd=random.choice(var)
    xd1=random.choice(var)
    if xd !=xd1:
        print(f"apuesta:{xd} y resultado={xd1} -> ACIERTAS")
        contador+=1
print("El numero de aciertos es: ",contador)

