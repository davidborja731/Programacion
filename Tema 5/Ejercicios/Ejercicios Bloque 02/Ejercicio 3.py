class raices:
    a=int
    b=int
    c=int
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def obtener_raices(self):
        calculo=(-self.b+((self.b)**2-(4*self.a*self.c))**0.5)/2*self.a
        calculo2=(-self.b-((self.b)**2-(4*self.a*self.c))**0.5)/2*self.a
        print(f"{calculo},{calculo2}")
    def obtener_raiz(self):
        calculo=(-self.b+((self.b)**2-(4*self.a*self.c))**0.5)/2*self.a
        calculo2=(-self.b-((self.b)**2-(4*self.a*self.c))**0.5)/2*self.a
        if calculo==calculo2:
            print(f"{calculo}")
    def determinante(self):
        calculo=(self.b**2)-4*self.a*self.c
        return calculo
    def tiene_raiz(self):
        if self.determinante()>0:
            return True
        else:
            return False
    def tiene_raizes(self):
        if self.determinante()==0:
            return True
        else:
            return False
    def calcular(self):
        if self.tiene_raiz():
            self.tiene_raiz()
        elif self.tiene_raizes():
            self.tiene_raizes()
        else:
            print("No existen raices")  
xd=raices(1,2,-3)
xd.obtener_raices()
xd.obtener_raiz()
xd.determinante()
xd.tiene_raizes()
xd.tiene_raiz()
xd.calcular()
