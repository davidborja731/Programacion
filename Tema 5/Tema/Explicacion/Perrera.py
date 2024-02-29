from Animales import perro as perro
class perrera:
    direccion=str
    jefe=str
    lista_perros = []
    def __init__(self,direccion,jefe):
        self.direccion=direccion
        self.jefe=jefe
    def dame_info(self):
        print(f"la perrera esta {self.direccion} y su jefe es {self.jefe}" f"Ahora tenemos {self.lista_perros}")
        for perro in self.lista_perros:
            perro.dame_info()
    def nuevo_perro(self,perro):
        self.lista_perros.append(perro)
    def muerto(self,perro):
        self.lista_perros.remove(perro)
        