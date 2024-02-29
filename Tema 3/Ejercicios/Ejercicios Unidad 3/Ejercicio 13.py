num1=int(input("Dime un numero "))
num2=int(input("Dime otro numero "))
def poder(num1,num2):
    for i in range(num2+1):
        resultado=num1**i
    return resultado
print(poder(num1,num2))
