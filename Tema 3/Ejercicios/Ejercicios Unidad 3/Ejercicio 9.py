def imprimir_fichas_domino():
    for i in range(7):
        for j in range(i,7):
            print(f"{i}|{j}",end=" ")
        print()
        
def main():
    imprimir_fichas_domino()

main()
