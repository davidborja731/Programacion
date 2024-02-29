nombres = []
edades = []
nombre = ""
while nombre != "*":
    nombre = input("Ingresa el nombre del alumno: ")
    if nombre != "*":
        nombres.append(nombre)
        edad = int(input("Ingresa una edad: "))
        edades.append(edad)
mayor = edades[0]
print("Alumnos mayores de edad: ")
for i in range(0,len(edades)):
    if edades[i] >= 18:
        print(f"{nombres[i]} tiene {edades[i]} años")
        if edades[i] > mayor:
            mayor = edades[i]
            nombreMayor = nombres[i]
print(f"{nombreMayor} tiene la mayor edad {mayor} años")

    

