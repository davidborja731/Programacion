from Balones import balones as balones
from Chandal import chandal as chandal
from Camisetas import camiseta as camiseta
from Pantalones import pantalon as pantalon
class tienda(balones,chandal,camiseta,pantalon):
    listabalon=[]
    listachandal=[]
    listacamiseta=[]
    listapantalon=[]
    n_balones=int
    n_chandal=int
    n_camisetas=int
    n_pantalones=int
    def __init__(self, n_balones, n_chandal, n_camisetas, n_pantalones, listabalon, listachandal, listacamiseta, listapantalon,identificador, Marca, modelo, tipodeporte, precio, color, talla, tipo, composicion):
        super().__init__(identificador, Marca, modelo, tipodeporte, precio, color, talla, tipo, composicion)
        self.listabalon=listabalon
        self.listachandal=listachandal
        self.listacamiseta=listacamiseta
        self.listapantalon=listapantalon
        self.n_balones=n_balones
        self.n_chandal=n_chandal
        self.n_camisetas=n_camisetas
        self.n_pantalones=n_pantalones
    def añadir(self):
        if self.identificador==1:
            self.listabalon.append(self.identificador)
        elif self.identificador==2:
            self.listachandal.append(self.identificador)
        elif self.identificador==3:
            self.listacamiseta.append(self.identificador)
        elif self.identificador==4:
            self.listapantalon.append(self.identificador)
balon=balones(1,"Nike",34, "tenis",45)
balon.mostrar()
        