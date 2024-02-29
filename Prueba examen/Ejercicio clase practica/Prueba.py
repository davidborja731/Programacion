class Persona:
    def __init__(self, nombre, apellidos, dni, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono

class Alumno(Persona):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, evaluacion_continua):
        super().__init__(nombre, apellidos, dni, direccion, telefono)
        self.evaluacion_continua = evaluacion_continua
        self.clase = None

class Profesor(Persona):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, asignaturas, horario):
        super().__init__(nombre, apellidos, dni, direccion, telefono)
        self.asignaturas = asignaturas
        self.horario = horario

class Director(Profesor):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, asignaturas, horario, complemento, horas_semanales, anos_director):
        super().__init__(nombre, apellidos, dni, direccion, telefono, asignaturas, horario)
        self.complemento = complemento
        self.horas_semanales = horas_semanales
        self.anos_director = anos_director

class JefeEstudios(Profesor):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, asignaturas, horario, complemento, localizable):
        super().__init__(nombre, apellidos, dni, direccion, telefono, asignaturas, horario)
        self.complemento = complemento
        self.localizable = localizable

class Clase:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def matricular(self, alumno):
        if len(self.alumnos) < 30:
            self.alumnos.append(alumno)
            alumno.clase = self
        else:
            print("La clase está llena.")

    def dar_baja(self, alumno):
        self.alumnos.remove(alumno)
        alumno.clase = None

    def buscar_alumno(self, dni):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                return alumno
        return None

    def quitar_evaluacion_continua(self, dni):
        alumno = self.buscar_alumno(dni)
        if alumno:
            alumno.evaluacion_continua = False

    def mostrar_informacion(self):
        print(f"Clase: {self.nombre}")
        for alumno in self.alumnos:
            print(f"Alumno: {alumno.nombre} {alumno.apellidos}")

class Instituto:
    def __init__(self, direccion, telefono, director, jefe_estudios):
        self.direccion = direccion
        self.telefono = telefono
        self.director = director
        self.jefe_estudios = jefe_estudios
        self.clases = []

    def agregar_clase(self, clase):
        self.clases.append(clase)

    def buscar_clase(self, nombre):
        for clase in self.clases:
            if clase.nombre == nombre:
                return clase
        return None

    def matricular_alumno(self, nombre_clase, alumno):
        clase = self.buscar_clase(nombre_clase)
        if clase:
            clase.matricular(alumno)

    def mostrar_informacion(self):
        print(f"Instituto: {self.direccion}")
        print(f"Director: {self.director.nombre} {self.director.apellidos}")
        print(f"Jefe de Estudios: {self.jefe_estudios.nombre} {self.jefe_estudios.apellidos}")
        for clase in self.clases:
            clase.mostrar_informacion()

# Crear personas
director = Director("Juan", "Pérez", "12345678A", "Calle Falsa 123", "987654321", ["Matemáticas", "Física"], "Mañana y tarde", 1000, 40, 5)
jefe_estudios = JefeEstudios("Ana", "Gómez", "87654321B", "Avenida Siempre Viva 456", "123456789", ["Lengua", "Historia"], "Vespertino", 500, True)
alumno1 = Alumno("Pedro", "García", "23456789C", "Plaza Mayor 789", "234567890", True)
alumno2 = Alumno("María", "López", "34567890D", "Paseo de la Castellana 101112", "345678901", True)

# Crear clases
dam1 = Clase("DAM1")
dam2 = Clase("DAM2")
smr1 = Clase("SMR1")
smr2 = Clase("SMR2")

# Crear instituto
instituto = Instituto("Gran Vía 123", "567890123", director, jefe_estudios)

# Agregar clases al instituto
instituto.agregar_clase(dam1)
instituto.agregar_clase(dam2)
instituto.agregar_clase(smr1)
instituto.agregar_clase(smr2)

# Matricular alumnos
instituto.matricular_alumno("DAM1", alumno1)
instituto.matricular_alumno("DAM2", alumno2)

# Buscar un alumno y quitarle la evaluación continua
dam1.quitar_evaluacion_continua("23456789C")

# Dar de baja a un alumno
dam2.dar_baja(alumno2)

# Mostrar información del instituto
instituto.mostrar_informacion()
