vocal=input("Dime una palabra ")
def contar(vocal):
    vocales=0
    xd="aeiou"
    for letra in vocal:
        if letra.lower() in xd:
            vocales += 1
    return vocales
contadores=contar(vocal)
print(f"En la cadena {vocal} hay {contadores} vocales.")
