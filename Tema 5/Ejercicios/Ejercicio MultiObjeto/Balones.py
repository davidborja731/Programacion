class balones:
    valor_objeto=1
    identificador=valor_objeto
    Marca=str
    modelo=str
    tipodeporte=str
    precio=str
    def __init__(self, identificador,Marca,modelo,tipodeporte,precio):
        self.identificador=identificador
        self.Marca=Marca
        self.modelo=modelo
        self.tipodeporte=tipodeporte
        self.precio=precio
    def mostrar(self):
        print(f"El identificador es {self.identificador} su marca es {self.Marca} es el modelo {self.modelo} es para el deporte {self.tipodeporte} y su precio es {self.precio}")
balon=balones(1,"Nike",34, "tenis",45)
balon.mostrar()