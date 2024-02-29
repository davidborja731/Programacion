class persona:
    def __init__(self,nombre,apellidos,dni,direccion,telefono):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.direccion=direccion
        self.telefono=telefono
class alumno(persona):
    def __init__(self,nombre,apellidos,dni,direccion,telefono,evaluacion:bool):
        super().__init__(nombre,apellidos,dni,direccion,telefono)
        self.evaluacion=evaluacion
    def continua(self):
        if self.evaluacion == True:
            print("El alumno tiene evaluacion continua")
        elif self.evaluacion == False:
            print("El alumno no tiene evaluacion continua")
class Clase:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def matricular(self, alumno):
        if alumno.dni in [a.dni for a in self.alumnos]:
            print("El dni", alumno.dni, "ya esta matriculado")
        else:
            self.alumnos.append(alumno)

    def imprimir_alumnos(self):
        print([alumno.dni for alumno in self.alumnos])



alumno1=alumno("juan","perez","12345678A","Calle 1234","654321343",True)
alumno2=alumno("Pepe","alejandro","12345678A","Calle 1234","654321343",True)
DAM1=Clase("DAM1")
DAM1.matricular(alumno1)

