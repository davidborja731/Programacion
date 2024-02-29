cuenta=int(input("Dime cuantos valores quieres introducir: "))
xd=0
lista=[]
while xd < cuenta:
      xd+=1
      if xd > 0:
            palabra=input("Dime la palabra: ")
            lista.append(palabra)
if cuenta==0:
      print("Imposible")
else:
      palabraacontar=input("Dime la palabra a buscar: ")
      cuenta=lista.count(palabraacontar)
      print("la palabra",palabraacontar,"Aparece",cuenta,"veces.")
      print("La tabla final es",lista)