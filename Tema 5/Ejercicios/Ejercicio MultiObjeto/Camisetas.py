from Chandal import chandal as chandal


class camiseta(chandal):
    valor_objeto = 3
    identificador = valor_objeto
    talla = str
    tipo = chr("corta", "larga", "tecnica", "tirantes", "termica", "natacion")
    composicion = chr("algodon", "poliester", "reciclada")

    def __init__(self, identificador, Marca, modelo, tipodeporte, precio, color, talla, tipo, composicion) -> None:
        super().__init__(identificador, Marca, modelo, tipodeporte, precio, color)
        self.talla = talla
        self.tipo = tipo
        self.composicion = composicion

    def mostrar(self):
        print(
            f"El identificador es {self.identificador} su marca es {self.Marca} es el modelo {self.modelo} es para el deporte {self.tipodeporte} y su precio es {self.precio} y su color es {self.color} es de la talla {self.talla} del tipo {self.tipo} su composicion es {self.composicion}")
