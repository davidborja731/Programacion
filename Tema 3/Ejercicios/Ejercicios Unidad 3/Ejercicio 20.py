num1=int(input("Dime un numero "))
def factorial(num1):
    for i in range(1, num1 + 1):
        num1*= i
    return num1
print(factorial(num1))