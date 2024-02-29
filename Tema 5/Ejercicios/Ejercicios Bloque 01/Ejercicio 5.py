class calculadora:
    numero1=int
    numero2=int
    def __init__(self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2
    def suma(self):
        suma=self.numero1+self.numero2
        print(f"La suma de {self.numero1} y {self.numero2} es igual a {suma}")
    def resta(self):
        resta=self.numero1-self.numero2
        print(f"La resta de {self.numero1} y {self.numero2} es igual a {resta}")
    def multiplicacion(self):
        multiplicacion=self.numero1*self.numero2
        print(f"La multiplicacion de {self.numero1} y {self.numero2} es igual a {multiplicacion}")
    def division(self):
        division=self.numero1/self.numero2
        print(f"La division de {self.numero1} y {self.numero2} es igual a {division}")
numeros=calculadora(10,2)
numeros.suma()
numeros.resta()
numeros.multiplicacion()
numeros.division()