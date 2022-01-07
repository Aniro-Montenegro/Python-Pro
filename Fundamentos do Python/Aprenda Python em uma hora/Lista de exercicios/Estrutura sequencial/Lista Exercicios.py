'''









Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
'''

# 1- Faça um Programa que mostre a mensagem "Alo mundo" na tela.


palavra = " Alo mundo"

print(palavra)

# 2 -Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input("Digite um numero: ")
print(f'O número digitado foi :{numero}\n')

# 3- Faça um Programa que peça dois números e imprima a soma.

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
print(f'A soma dos numeros é igual: {numero1 + numero2}\n')

# 4- Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Digite a nota de Matemática: "))
nota2 = int(input("Digite a nota de Português: "))
nota3 = int(input("Digite a nota de Filosofia: "))
nota4 = int(input("Digite a nota de História: "))
print(f'A média das notas é igual a : {(nota4 + nota3 + nota2 + nota1) / 4}\n')

# 5 - Faça um Programa que converta metros para centímetros.

metros = float(input("Digite a quantidade de metros: "))

print(f'{metros} em centímetros = {metros * 100}\n')

# 6 -Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Digite o valor do raio do circulo: "))

print(f'A área do raio={raio}  = {3.14 * raio}\n')

# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o valor do lado do quadrado: "))

print(f'O dobro da area do quadrado ={2 * (lado * lado)}\n')

# 8- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


hora = float(input("Quanto você ganha por hora? :  "))
mes = float(input("Quantas hora você trabalhou este mês? :  "))

print(f'O seu salário é de = R${hora * mes}\n')

# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temperatura = float(input("Digite a temperatura em Fahrenheit :  "))

print(f'A temperatura de {temperatura} Fahrenheit é em Celsius = {5 * (temperatura - 32) / 9}º\n')

# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temperatura = float(input("Digite a temperatura em Celsius :  "))

print(f'A temperatura de {temperatura} Celsius é em Fahrenheit = {(temperatura*9/5)+32}º\n')

# 11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo

inteiro1 = int(input("Digite um numero inteiro :  "))
inteiro2 = float(input("Digite outro numero inteiro :  "))
flutuante = float(input("Agora digite um numero real :  "))


print(f'O produto do dobro de {inteiro1} com metade de {inteiro2}  = {(inteiro1*2)*(inteiro2/2)}')
print(f'A soma do triplo de {inteiro1} com {flutuante}.  = {(inteiro1*3)+flutuante}')
print(f'O numero {flutuante} elevado ao cubo..  = {flutuante**3}\n')

# 12 -Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = int(input("Digite sua altura em centimetros :  "))

print(f'O seu peso ideal é {(72.7*altura/100) - 58}\n')

# 13 -Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

altura = int(input("Digite sua altura em centimetros :  "))

print(f'Peso ideal homens:  {(72.7*altura/100) - 58}')
print(f'Peso ideal mulheres:  {(62.1*altura/100) - 44.7}\n')

# 14 -João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso
# (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

estabelecido=50
multa=4

peixes = float(input("Digite o peso dos peixes pescados :  "))
diferenca=peixes-50

if diferenca>0:
    print(f"Excesso de peixes Kg {diferenca}")
    print(f"Multa R${diferenca*multa}\n")




