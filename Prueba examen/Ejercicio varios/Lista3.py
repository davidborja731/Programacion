#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#asignaturas_a_repetir = []
#for asignatura in asignaturas:
    #nota = float(input(f"Introduce la nota que has sacado en {asignatura}: "))
    #if nota < 5:
        #asignaturas_a_repetir.append(asignatura)
#for asignatura in asignaturas_a_repetir:
    #asignaturas.remove(asignatura)
#print("Las asignaturas que tienes que repetir son:", asignaturas_a_repetir)

#alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#for i in range(len(alphabet),1,-1):
    #if i%3==0:
        #alphabet.pop(i-1)
#print(alphabet)

#palabra = input("Introduce una palabra: ")
#lista_palabra = list(palabra)
#lista_inversa = list(reversed(palabra))
#if lista_palabra == lista_inversa:
    #print("La palabra introducida es un palíndromo.")
#else:
    #print("La palabra introducida no es un palíndromo.")
#vector1 = [1, 2, 3]#vector2 = [-1, 0, 2]#producto = 0#for i, j in zip(vector1,vector2):
#producto += i*j
#print(f"El producto de {vector1} y {vector2} es {producto}")

dias = [31,28,31,30,31,30,31,31,30,31,30,31]
nombre_mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
while True:
    mes = int(input("Introduce un mes (1-12):"))
    if mes < 1 or mes > 12:
	    print("Error: mes incorrecto.")
    elif mes>=1 and mes<= 12:
        print("correcto")
        break
print("El mes de",nombre_mes[mes-1],"tiene",dias[mes-1],"días.")

