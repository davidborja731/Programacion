numero1=int(input("introduce un numero: "))
numero2=int(input("introduce otro numero: "))
mayor= max(numero1, numero2)
print(mayor)
menor=min(numero1, numero2)
print(menor)
resto=mayor%menor
prueba=resto==0
if prueba== True:
    print("Es multiplo")
else:
    print("No es multiplo")

