num1=int(input("Dime un numero "))
def factorial(num1):
    if num1==0:
        return 1
    else:
        num1*factorial(num1-1)
        return num1
def sumafactorial(num1):
    suma=0
    for i in range(1, num1 + 1):
        suma+=factorial(i)
    return suma
print(sumafactorial(num1))