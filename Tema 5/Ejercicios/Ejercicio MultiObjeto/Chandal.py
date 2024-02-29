from Balones import balones as balones
class chandal(balones):
    valor_objeto=2
    identificador=valor_objeto
    color=str
    def __init__(self, identificador, Marca, modelo, tipodeporte, precio,color) -> None:
        super().__init__(identificador, Marca, modelo, tipodeporte, precio)
        self.color=color
    def mostrar(self):
        print(f"El identificador es {self.identificador} su marca es {self.Marca} es el modelo {self.modelo} es para el deporte {self.tipodeporte} y su precio es {self.precio} y su color es {self.color}")

