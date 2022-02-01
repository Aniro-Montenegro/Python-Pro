def imprimir_triangulo_de_numeros(n: int):
    palavra = ""
    x = 1
    for a in range(n):
        palavra += (str(x) + "   ")
        x+=1
    n -= 1
    if n < 0:
        return
    else:
        imprimir_triangulo_de_numeros(n)
    print(palavra)

imprimir_triangulo_de_numeros(10)