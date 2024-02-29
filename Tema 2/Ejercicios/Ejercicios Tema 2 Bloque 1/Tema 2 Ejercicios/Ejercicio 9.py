super1=int(input("Dime un numero: "))
super2=int(input("Dime un numero: "))
xd=max(super1,super2)
xd1=min(super1,super2)
resta=xd-xd1
if xd == super1:
    print("El primero es mayor ","El resultado es ", resta)
if xd == super2:
    print("El segundo es mayor ","El resultado es ", resta)