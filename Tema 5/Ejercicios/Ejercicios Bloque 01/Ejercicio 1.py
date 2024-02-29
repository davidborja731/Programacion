class persona:
    nombre=str
    edad=int
    DNI=str
    def __init__(self, nombre, edad, DNI):
        self._nombre = nombre
        self._edad = edad
        self._DNI = DNI

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def DNI(self):
        return self._DNI

    @DNI.setter
    def DNI(self, DNI):
        self._DNI = DNI

    def mostrar(self):
        print(f"Mi nombre es {self._nombre}. Tengo {self._edad} años y mi DNI es {self._DNI}")
    def mayor(self):
        if self.edad >= 18:
            print("Es mayor de edad") 
        else:
            print("Es menor de edad")   
persona1 = persona("Paco", 18, "34567890B")
persona1.mostrar()
persona1.mayor()

