class alumno:
    nombre=str
    nota=float
    def __init__(self, nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def mostrar(self):
        if self.nota < 5:
            print(f"El alumo se llama {self.nombre} tiene un {self.nota} y esta suspenso.")
        else:
            print(f"El alumo se llama {self.nombre} tiene un {self.nota} y esta aprobado.")
alumno1=alumno("pepe",3)
alumno1.mostrar() 