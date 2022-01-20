'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

numero = 0
lista = []
while True:
    numero = float(input('Digite um numero'))
    if numero == -1:
        break
    lista.append(numero)

tamanho = len(lista)

print(f'Foram lidas {tamanho} notas')

print(' '.join([str(nota) for nota in lista]))

lista.reverse()

for nota in lista:
    print(nota)

soma = sum(lista)
print(f'Soma das notas é : {soma}')

print(f'Soma das notas é : {soma} e a média dos valoes é {soma/len(lista)}')
media=soma/len(lista)
print(f'Notas acima da média')
print(' '.join([str(nota) for nota in lista if nota > media]))

print(f'Notas abaixo de 7')
print(' '.join([str(nota) for nota in lista if nota < 7]))

print("Encerrado o programa")