def imprimir_triangulo_de_numeros(n: int):
    palavra = (str(n) + " ") * n
    n -= 1
    if n < 0:
        return
    else:
        imprimir_triangulo_de_numeros(n)
    print(palavra)


imprimir_triangulo_de_numeros(5)
imprimir_triangulo_de_numeros(6)
