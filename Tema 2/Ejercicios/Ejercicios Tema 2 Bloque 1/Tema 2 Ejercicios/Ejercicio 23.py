num1= int(input("Dame un numero: "))
def factorial(num1):
    if num1 <= 0:
        return 1
    factorial = 1
    while num1 > 0:
        factorial = factorial * num1
        num1 -= 1
    return factorial

def factorial_recursivo(num1):
    if num1 <= 1:
        return 1
    return num1 * factorial(num1)


valor = num1
f = factorial(valor)
print(f"El factorial de {valor} es {f}")
f = factorial(valor)
print(f"El factorial (calculado de manera recursiva) de {valor} es {f}")