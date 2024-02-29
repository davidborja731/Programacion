class libro:
    ISBN:str
    Titulo:str
    Autor:str
    paginas: str
    def __init__(self,ISBN,Titulo,Autor,Paginas) -> None:
        self.ISBN=ISBN
        self.Titulo=Titulo
        self.Autor=Autor
        self.paginas=Paginas
    @property
    def ISBN(self): 
        return self._ISBN
    @ISBN.setter
    def ISBN(self, ISBN):   
        self._ISBN = ISBN

    @property
    def Titulo(self):
        return self._Titulo
    @Titulo.setter
    def Titulo(self, Titulo):
        self._Titulo = Titulo
    @property
    def Autor(self):
        return self._Autor
    @Autor.setter
    def Autor(self, Autor):
        self._Autor = Autor
 
    @property
    def paginas(self):
        return self._paginas
    @paginas.setter
    def paginas(self, paginas):
        self._paginas = paginas
    def mostrar(self):
        print(f"El libro {self.Titulo} con {self.ISBN} creado por el autor {self.Autor} tiene {self.paginas} paginas")
