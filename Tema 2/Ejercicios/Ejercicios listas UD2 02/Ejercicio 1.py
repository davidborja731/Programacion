letra=input("Dime una letra: ")
if letra.isdigit():
    print("Numero entero")
elif letra.isalpha():
    print("letra")
else:
    try:
        float(letra)
        print("Numero real")
    except ValueError:
        print("No es nada")