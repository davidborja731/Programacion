letra=input("Dime la letra: ")
anchura=int(input("Dime la anchura: "))
def triangulo(letra, anchura):
    for i in range(anchura, 0, -1):
        print(letra * i)
triangulo(letra, anchura)
