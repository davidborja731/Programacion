a=int(input("Dame un coeficiente a: "))
b=int(input("Dame un coeficiente b: "))
c=int(input("Dame un coeficiente c: "))
disc=b*b-4*a*c
if disc>0:
    print("No tiene solucion")
else:
    raiz=disc
    x1=(-b+raiz)/(2 * a)
    x2=(-b-raiz)/(2*a)
    print("x1 es: ",x1,"x2 es: ",x2)
