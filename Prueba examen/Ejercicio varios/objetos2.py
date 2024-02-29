class cuenta:
    def __init__(self, Titular, cuenta=0.0):
        self._Titular=Titular
        self._cuenta= cuenta
    @property
    def Titular(self):
        return self._Titular
    @Titular.setter
    def Titular(self,Titular):
        self._Titular=Titular

    @property
    def cuenta(self):
        return self._cuenta
    @cuenta.setter
    def Titular(self, cuenta):
        self._cuenta = cuenta
    def mostrar(self):
        print(f"Titular: {self._Titular} Cantidad: {self._cuenta}")
    def ingresar(self):
        cantidad=float(input("Cuanto quieres ingresar: "))
        if cantidad <= 0:
            print("No se puede ingresar esa cantidad")
        else:
            self._cuenta+=cantidad
        print(f"Tienes en tu cuenta {self._cuenta}")
    def retirar(self):
        cantidad=float(input("Cuanto quieres sacar: "))
        if cantidad <= 0:
            print("No se puede retirar esa cantidad")
        else:
            self._cuenta -= cantidad
        print(f"Tienes en tu cuenta {self._cuenta}")
cuenta1=cuenta("juan andres")
cuenta1.mostrar()
cuenta1.ingresar()
cuenta1.retirar()
