class cuenta:
    titular=str
    cantidad=float
    def __init__(self,titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad
        self.dinero=cantidad
    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self, titular):
        self._titular = titular
    def mostrar(self):
        print(f"El titular es {self.titular} y tiene {self.cantidad} de dinero")
    def retirada(self):
        retiro=float(input("¿Cuanto quieres retirar? "))
        if retiro == 0:
            print(f"Tienes {self.cantidad} en tu cuenta")
            return self.cantidad
        elif retiro > 0:
            self.cantidad-=retiro
            print(f"Ahora tienes en tu cuenta {self.cantidad}") 
    def ingreso(self):
        ingreso=float(input("¿Cuanto quieres ingresar? "))
        if ingreso == 0:
            print(f"Tienes {self.cantidad} en tu cuenta")
            return self.cantidad
        elif ingreso > 0:
            self.cantidad+=ingreso
            print(f"Ahora tienes en tu cuenta {self.cantidad}") 
        else:
            print("No puedes ingresar cantidades negativas")
            print(f"Tienes {self.cantidad} en tu cuenta")
cuenta1=cuenta("",2590)
cuenta1.mostrar()
cuenta1.retirada()
cuenta1.ingreso()