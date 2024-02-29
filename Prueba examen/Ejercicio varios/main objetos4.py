lista=["Antonio","Juan","Juan","Pedro","Lucas","Ana","Julian","Ana","Ana","Juan","Ana","Ana"]
for x in lista:
    buscar=x
    comprobar=lista.count(buscar)
    if comprobar > 2:
        lista.remove(buscar)
print(lista)