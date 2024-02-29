a = int(input("Dame un numero: "))
b = int(input("Dame un numero: "))
def maximo(a, b):
    temporal=0
    while b !=0:
        temporal=b
        b=a%b
        a=temporal
    return a
print("El maximo comun divisor es",maximo(a,b))