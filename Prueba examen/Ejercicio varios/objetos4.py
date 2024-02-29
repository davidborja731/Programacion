class agenda:
    def __init__(self, nombre, telefono,contactos=[]):
        self._nombre=nombre
        self._telefono=telefono
        self._contactos=contactos
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre

    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono
    def añadir(self):
        self._contactos.append(self._nombre)
    def buscar(self):
        busqueda=input("¿Que contacto quieres buscar? ")
        comprobacion=self._contactos.index(busqueda)
        if comprobacion == True:
            print("El contacto si existe")
        else:
            print("El contacto no existe")
    def mostrar(self):
        print(self._contactos)
    def buscamos(self):
        busqueda=input("¿Que contacto quieres buscar? ")
        comprobacion=self._contactos.index(busqueda)
        if comprobacion == True:
            print(f"{self._telefono}")
        else:
            print("El contacto no existe")
    def eliminar(self):
        elimina = input("¿Que contacto quieres eliminar? ")
        self._contactos.remove(elimina)
contacto1 = agenda("Juan", "978908765")
contacto2 = agenda("Pepe", "876543219")
contacto3 = agenda("Luis", "908765432")
contacto1.añadir()
contacto1.mostrar()
contacto2.añadir()
contacto2.mostrar()
contacto3.añadir()
contacto3.mostrar()
contacto3.buscar()
contacto3.buscamos()
contacto3.eliminar()