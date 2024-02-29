from Ejercicio1 import libro as libro 

    
libro1=libro("9786564","El quijote","Anonimo","876")
libro2=libro("8546344","El señor de los anillos","Tolkien","893")
libro1.mostrar()
libro2.mostrar()
if libro.paginas >libro2.paginas:
    print("El libro uno tiene mas paginas")
else:
    print("El libro2 uno tiene mas paginas")