class triangulo:
    lado_izquierdo=int
    lado_derecho=int
    base=int
    def __init__(self,lado_izquierdo,lado_derecho,base):
        self.lado_izquierdo=lado_izquierdo
        self.lado_derecho=lado_derecho
        self.base=base
    def mostrar(self):
        if self.lado_derecho == self.lado_izquierdo and self.lado_derecho==self.base:
            print(f"El triangulo tiene un lado de {self.lado_derecho} otro de {self.lado_izquierdo} y su base mide {self.base} es un triangulo equilatero")
        elif self.base != self.lado_derecho and self.lado_derecho!=self.lado_izquierdo and self.base!=self.lado_izquierdo:
            print(f"El triangulo tiene un lado de {self.lado_derecho} otro de {self.lado_izquierdo} y su base mide {self.base} es un triangulo escaleno")
        else:
            print(f"El triangulo tiene un lado de {self.lado_derecho} otro de {self.lado_izquierdo} y su base mide {self.base} es un triangulo isosceles ")
    
triangulo1=triangulo(4,4,4)
triangulo2=triangulo(4,6,4)
triangulo3=triangulo(5,6,2)
triangulo1.mostrar()
triangulo2.mostrar()
triangulo3.mostrar()
