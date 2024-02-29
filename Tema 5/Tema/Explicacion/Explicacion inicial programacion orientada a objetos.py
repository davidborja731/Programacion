class persona:
    nombre=""
    altura=0
    peso=0
    color_pelo=""
    edad=0
    def __init__(self, nombre, altura, peso, color_pelo, edad):
        self.nombre=nombre
        self.altura=altura
        self.peso=peso
        self.color_pelo=color_pelo
        self.edad=edad
    def mostrar(self):
        print(f"La persona tiene el nombre de {self.nombre} tiene una edad de {self.edad} su altura es {self.altura} su peso es {self.peso} su color de pelo es {self.color_pelo} su edad es {self.edad}")
    def esmayor(self)->bool:
        if self.edad >=18:
            return True
        else:
            return False
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
    @property
    def altura(self):
        return self.__altura
    @nombre.setter
    def altura(self, altura):
        self.__altura=altura
    @property
    def peso(self):
        return self.__peso
    @nombre.setter
    def peso(self, peso):
        self.__peso=peso
    @property
    def color_pelo(self):
        return self.__color_pelo
    @nombre.setter
    def color_pelo(self, color_pelo):
        self.__color_pelo=color_pelo
    @property
    def edad(self):
        return self.__edad
    @nombre.setter
    def edad(self, edad):
        self.__edad=edad
david=persona("david",160,58,"Rubio",19)
pepe=persona("pepe",123,90,"Marron",9)
juana=persona("juana",190,20,"Rojo",89)
print(david.nombre)
print(pepe.nombre)
print(juana.nombre)
david.mostrar()
pepe.mostrar()
juana.mostrar()
print(david.esmayor())
print(pepe.esmayor())
print(juana.esmayor())
print(david.nombre)