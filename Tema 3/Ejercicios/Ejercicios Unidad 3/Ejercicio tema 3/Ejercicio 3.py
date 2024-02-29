numero1= 0
numero2= 1
for i in range(100000000):
    if numero1 <= 100000000000000:
        print(numero1)
        numero1, numero2 =numero2, numero1 + numero2
