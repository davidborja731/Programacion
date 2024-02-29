multiplo=[]
for x in range(25001):
    if x % 41:
        multiplo.append(x)
print(multiplo)
listacompra=["Agua","huevos","Aceite"]
listacompra.insert(100,"jamon")
listacompra.insert(10,"Pan")
print(listacompra[0:10])
listacena=["Ensalada","Pizza","Postre"]
listacompra+=listacena
listacompra.append("Limon")
listacompra[0]="magnalena"
listacompra.remove("Limon")
listacompra.pop()
print(listacompra)
