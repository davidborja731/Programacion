texto=input("introduce un texto: ")
palabra=[]
for letra in texto:
    if letra in palabra:
        print("No es un isograma")
        break
    palabra.append(letra)
else:
    print("Es un isograma")

