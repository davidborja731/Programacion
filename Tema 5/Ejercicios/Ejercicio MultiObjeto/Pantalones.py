from Chandal import chandal as chandal
class pantalon(chandal):
    valor_objeto=4
    identificador=valor_objeto
    longitud=str
    def __init__(self, identificador, Marca, modelo, tipodeporte, precio, color,talla,tipo,composicion) -> None:
        super().__init__(identificador, Marca, modelo, tipodeporte, precio, color)
        self.talla=talla
        self.tipo=tipo
        self.composicion=composicion
    def mostrar(self):
        print(f"El identificador es {self.identificador} su marca es {self.Marca} es el modelo {self.modelo} su "
              f"precio es {self.precio} su color es {self.color} es de la talla {self.talla} su longit"
              f"ud es {self.longitud}")