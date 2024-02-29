class electrodomestico:
    def __init__(self, color="blanco", consumo="F", preciobase=100, peso=5):
        self._color=color
        self._consumo=consumo
        self._preciobase=preciobase
        self._peso=peso
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def consumo(self):
        return self._consumo
    @consumo.setter
    def consumo(self, consumo):
        self._consumo = consumo

    @property
    def preciobase(self):
        return self._preciobase
    @preciobase.setter
    def consumo(self, preciobase):
        self._preciobase = preciobase

    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self, peso):
        self._peso = peso
    def consumos(self):
        lista = ["A", "B", "C", "D", "E", "F"]
        if self._consumo in lista:
            return self._consumo
        else:
            self._consumo = "F"
    def colores(self):
        lista = ["Blanco", "Negro", "Rojo", "Azul", "Gris"]
        if self._color in lista:
            return self._color
        else:
            self._color = "Blanco"
    def precios(self):
        if self._consumo == "A":
            self._preciobase += 100
        elif self._consumo == "B":
            self._preciobase += 80
        elif self._consumo == "C":
            self._preciobase += 60
        elif self._consumo == "D":
            self._preciobase += 50
        elif self._consumo == "E":
            self._preciobase += 30
        elif self._consumo == "F":
            self._preciobase += 10
        if self._peso > 0 and self._peso <= 19:
            self._preciobase += 10
        elif self._peso >= 20 and self._peso <= 49:
            self._preciobase += 50
        elif self._peso >= 50 and self._peso <= 79:
            self._preciobase += 80
        elif self._peso >= 80:
            self._preciobase += 100
        print(f"El precio ahora es de {self._preciobase} su color es {self._color} su peso es {self._peso} y su consumo es {self._consumo}")
lavadora = electrodomestico("Amarillo","D",580,90 )
lavadora.consumos()
lavadora.colores()
lavadora.precios()