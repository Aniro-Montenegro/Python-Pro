def contar_caracteres(s):
    """
    Função que conta os caracteres de uma string
    Ex:
     contar_caracteres('Aniro')
   { 'a':1, 'i':1, 'n':1, 'o':1, 'r':1}
    :param s: string a ser contada

    """

    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    resultado={}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:

            resultado[caracter_anterior]=contagem
            caracter_anterior = caracter
            contagem = 1
    resultado[caracter_anterior]=contagem
    return  resultado


if __name__ == '__main__':
    print(contar_caracteres('Banana'))

