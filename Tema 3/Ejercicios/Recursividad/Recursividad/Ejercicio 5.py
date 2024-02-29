num1=int(input("Dime un numero "))
def primo(num1):
    for x in range(2, num1):
        if num1 % x == 0:
            return "No es primo"
    return "Es primo"
print(primo(num1))
            