num1=int(input("Dime un numero: "))
def recursiva(num1):
    if num1 == 0:
        return 0
    else:
        return num1%10+recursiva(num1 // 10)
print(recursiva(num1))