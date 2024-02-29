class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto {nombre} añadido correctamente.")

    def lista_de_contactos(self):
        print("Lista de contactos:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"Contacto encontrado: Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return
        print(f"No se encontró ningún contacto con el nombre {nombre}.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print(f"Contacto {nombre} actualizado correctamente.")
                return
        print(f"No se encontró ningún contacto con el nombre {nombre}.")

    def cerrar_agenda(self):
        print("Agenda cerrada. ¡Hasta luego!")




    

