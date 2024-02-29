class Electrodomestico:
    preciopre=100
    colorpre="blanco"
    consumopre="F"
    pesopre=5
    precio_base=preciopre
    color=colorpre
    consumo=consumopre
    peso=pesopre
    def __init__(self,precio_base,color,consumo,peso):
        self.precio_base=precio_base
        self.color=color
        self.consumo=consumo
        self.peso=peso
    def consumos(self):
        if self.consumo.upper() in ["A","B","C","D","E","F"]:
            print(self.consumo)
        else:
            self.consumo="F"
            print("F")
    def comprobarcolor(self):
        if self.color.lower() in ["balnco","negro","rojo","azul","gris"]:
            print(self.color)
        else:
            print("El color es incorrecto")
            self.color=self.color
    def preciofinal(self):
        if self.consumo=="A":
            self.precio_base+=100
        elif self.consumo=="B":
            self.precio_base+=80
        elif self.consumo=="C":
            self.precio_base+=60
        elif self.consumo=="D":
            self.precio_base+=50
        elif self.consumo=="E":
            self.precio_base+=30
        elif self.consumo=="F":
            self.precio_base+=10
        if self.peso >= 0 and self.peso <=19:
            self.precio_base+=10
            print("El precio es",self.precio_base)
        if self.peso >= 80:
            self.precio_base+=100
            print("El precio es",self.precio_base)
        if self.peso >= 20 and self.peso <=49:
            self.precio_base+=50
            print("El precio es",self.precio_base)
        if self.peso >= 50 and self.peso <=79:
            self.precio_base+=80
            print("El precio es",self.precio_base)
class lavadora(Electrodomestico):
    Kilos=5.0
    carga=Kilos
    def __init__(self, carga,precio_base,color,consumo,peso):
        super().__init__(precio_base,color,consumo,peso)
        self.carga=carga
    def preciofinal(self):
        if self.carga >=30:
            super().preciofinal()
            self.precio_base+=50
class televison(Electrodomestico):
    resolucion=float
    tamaño=20
    sintonizador=False
    def __init__(self,resolucion,tamaño,sintonizador,precio_base,color,consumo,peso):
        super().__init__(precio_base,color,consumo,peso)
        self.resolucion=resolucion
        self.tamaño=tamaño
        self.sintonizador=sintonizador
    def preciofinal(self):
        super().preciofinal()
        if self.resolucion>40:
            self.precio_base=self.precio_base*1.30
        if self.sintonizador==True:
            self.precio_base+=50






























lavadora=Electrodomestico(100,"Verde","A",5)
lavadora.consumos()
lavadora.comprobarcolor()
lavadora.preciofinal()
