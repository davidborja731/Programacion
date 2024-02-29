cuenta=int(input("Dime cuantos valores quieres introducir: "))
comp=0
lista=[]
while comp < cuenta:
        comp+=1
        if comp > 0:
            palabra=input("Dime la palabra: ")
            lista.append(palabra)
if cuenta==0:
      print("Imposible")
else:
    print("La tabla final es",lista)

