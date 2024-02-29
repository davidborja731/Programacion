num1=int(input("Dime un numero "))
def contar(num1):
    if num1 == 0:
        return "0"
    elif num1 > 0:
        print(num1)
        contar(num1-1)
contar(num1)