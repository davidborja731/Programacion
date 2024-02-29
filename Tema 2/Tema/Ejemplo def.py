def one():
    num1=2
    nu2=9
    return num1+nu2
print(one())
if one()==6:
    print("Funciona")
else:
    print("No funciona")
print("--------------------------------------------------")
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))