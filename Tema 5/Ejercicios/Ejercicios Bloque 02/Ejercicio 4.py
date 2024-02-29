import random
class persona:
    nombre=str
    edad=int
    dni=str
    sexo=chr
    peso=int
    altura=float

    def __init__(self,nombre,edad,sexo,peso,altura) -> None:
        self.nombre=nombre
        self.edad=edad
        self.dni=self.generadni
        self.sexo=sexo
        self.peso=peso
        self.altura=altura
    def calcularIMC(self):
        pesoideal=0
        pesobajo=-1
        pesoalto=1
        imc=self.peso/(self.altura)**2
        if imc <20:
            return pesobajo
        elif imc >=20 and imc <25:
            return pesoideal
        else:
            return pesoalto
    def mayoredad(self):
        if self.edad >18:
            return True
        else:
            return False
    def com_sexo(self):
        if self.sexo == "M" or "m" or self.sexo== "H" or "H":
            return True
        else:
            return False
    def informacion(self):
        print(f"{self.nombre},{self.edad} {self.sexo} {self.peso} {self.altura} {self.dni}")
    def generadni(self):
        numero=random.randint(0,99999999)
        letras='a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        posicion=numero%23
        letradni=letras[posicion]
        return str(numero)+letradni
persona1=persona("pepe",12,"M",70,1.78)
persona1.calcularIMC()
persona1.mayoredad()
persona1.com_sexo()
persona1.informacion()
persona1.generadni()