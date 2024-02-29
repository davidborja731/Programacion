class libro:
    def __init__(self, ISBN, Titulo, Autor, Paginas):
        self._ISBN = ISBN
        self._Titulo = Titulo
        self._Autor = Autor
        self._Paginas = Paginas

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
    def Paginas(self):
        return self._Paginas
    @Paginas.setter
    def Autor(self, Paginas):
        self._Paginas = Paginas

    def mostrar(self):
        print(f"El ISBN es {self._ISBN}, su título es {self._Titulo}, su autor es {self._Autor} y tiene {self._Paginas} páginas.")

