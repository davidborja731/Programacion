class Animal:
    numero_identificacion=str
    sexo=str
    def __init__(self,numero_identificacion,sexo):
        self.numero_identificacion=numero_identificacion
        self.sexo=sexo
    def hecer_sonido(self):
        print("Haciendo Sonido.......")
    def dame_info(self):
        print(f"soy un animal y tengo el numero; {self.numero_identificacion} y soy {self.sexo}")
class perro(Animal):
    raza=str

    def __init__(self,numero_identificacion,sexo,raza):
        super.__init__(numero_identificacion,sexo)
        self.raza=raza
    def hecer_sonido(self):
        print("Soy un perro y ladro.......")
    def dame_info(self):
        print(f"soy un animal y tengo el numero; {self.numero_identificacion} mi raza es {self.raza} y soy {self.sexo}")
    