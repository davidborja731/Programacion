num1=int(input("Dame un numero: "))
N=num1
def fibonacci(num1):
    if num1 <= 0:
        return 0
    elif num1 == 1:
        return 1
    else:
        xd=fibonacci(num1-1) + fibonacci(num1-2)
        return xd
def suma(N):
    suma = 0
    for i in range(N):
        suma += fibonacci(i)
    return suma
print(suma(N))