class cuenta:
    titular=str
    cantidad=float
    def __init__(self,titular, cantidad) -> None:
        self.titular=titular
        self.cantidad=cantidad
    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self, titular):
        self._titular = titular
    @property
    def cantidad(self): 
        return self.cantidad
    def mostrar(self):
        print(f"El titular es {self.titular} y tiene {self.cantidad} de dinero")
    def ingresar(self):
        cantidadintro=float(input("Cuanto dinero quieres meter: "))
        if cantidadintro > 0:
            self.cantidad+=cantidadintro
            print(f"La cantidad de dinero n la cuenta es {self.cantidad} ")
        else:
            print("No se pueden ingresar cantidades negativas")
    def retirada(self):
        cantidadreti=float(input("Cuanto dinero quieres sacar: "))
        self.cantidad-=cantidadreti
        if  self.cantidad <= 0:
            print("0")
            print("Tienes tu cuenta en numeros rojos")
        else:
            print(f"Ahora tienes en tu cuenta {self.cantidad} de euros")
cuenta1=cuenta("Antonio",1200)
cuenta1.mostrar()
cuenta1.ingresar()
cuenta1.retirada()
