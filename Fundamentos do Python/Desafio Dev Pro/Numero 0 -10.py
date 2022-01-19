"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.

"""

while True:
    try:
        numero = int(input("Digite um numero de 0 a 10\n"))
        if 0 <= numero <= 10:
            print(f"Nota {numero}")
            break
        else:
            print(f'Nota {numero} ')
    except ValueError:
        print("Valor invalido")
