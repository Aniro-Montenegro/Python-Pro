def imprimir_triangulo_de_numeros(n: int):
    for linha in range(1,n+1):
        for coluna in range(1,linha+1):
            print(coluna,end='   ')
        print('')

imprimir_triangulo_de_numeros(10)