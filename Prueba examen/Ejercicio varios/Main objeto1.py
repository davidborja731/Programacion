from objetos1 import libro as libro
libro1 = libro("9786542345", "El señor de los anillos", "Tolkien", 343)
libro1.mostrar()
libro2 = libro("9788976451", "El quijote", "Anonimo", 345)
libro2.mostrar()
def maspaginas():
    if libro1.Paginas > libro2.Paginas:
        print(f"El libro {libro1.Titulo} tiene mas paginas")
    elif libro2.Paginas > libro1.Paginas:
        print(f"El libro {libro2.Titulo} tiene mas paginas")
    else:
        print("Ambos tienen las mismas paginas")
maspaginas()