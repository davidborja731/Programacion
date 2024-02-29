suma = 0 
contador = 0 
while True: 
  numero = float(input("Introduce un número: ")) 
  if numero < 0: 
    break
  else: 
    suma += numero
    contador += 1
if contador > 0: 
  media = suma / contador
  print(f"La media de los {contador} números introducidos es {media}")
else: 
  print("No se ha introducido ningún número válido")
