num1=int(input("Dime un numero "))
def EscribirTablaMultiplicar(num1):
        for j in range(1, 11):
            print(f"{num1} x {j} = {num1*j}")
        print()
EscribirTablaMultiplicar(num1)