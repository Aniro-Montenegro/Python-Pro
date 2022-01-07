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

print(f'A temperatura de {temperatura} Celsius é em Fahrenheit = {(temperatura * 9 / 5) + 32}º\n')

# 11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo

inteiro1 = int(input("Digite um numero inteiro :  "))
inteiro2 = float(input("Digite outro numero inteiro :  "))
flutuante = float(input("Agora digite um numero real :  "))

print(f'O produto do dobro de {inteiro1} com metade de {inteiro2}  = {(inteiro1 * 2) * (inteiro2 / 2)}')
print(f'A soma do triplo de {inteiro1} com {flutuante}.  = {(inteiro1 * 3) + flutuante}')
print(f'O numero {flutuante} elevado ao cubo..  = {flutuante ** 3}\n')

# 12 -Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = int(input("Digite sua altura em centimetros :  "))

print(f'O seu peso ideal é {(72.7 * altura / 100) - 58}\n')

# 13 -Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

altura = int(input("Digite sua altura em centimetros :  "))

print(f'Peso ideal homens:  {(72.7 * altura / 100) - 58}')
print(f'Peso ideal mulheres:  {(62.1 * altura / 100) - 44.7}\n')

# 14 -João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso
# (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

estabelecido = 50
multa = 4

peixes = float(input("Digite o peso dos peixes pescados :  "))
diferenca = peixes - 50

if diferenca > 0:
    print(f"Excesso de peixes Kg {diferenca}")
    print(f"Multa R${diferenca * multa}\n")
else:
    print(f"Pescados {peixes}\n")

# 15 -Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

hora = float(input("Quanto você ganha por hora? :  "))
mes = float(input("Quantas hora você trabalhou este mês? :  "))
salario_bruto = hora * mes
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
ir = salario_bruto * 0.11
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'''
    Salario Bruto = R$ {salario_bruto},
    Salario Liquido = R$ {salario_liquido},
    INSS = R$ {inss}
    Imposto de Renda = R$ {ir},
    Sindicato = R$ {sindicato}
    
''')

# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e
# o preço total.

area = float(input("Qual o tamanho da área a ser pintada? :  "))
litros = area / 3

latas = 0

if litros % 18 == 0:
    latas = litros / 18
else:
    latas = (litros // 18) + 1

print(f'Serão comprada(s) {int(latas)} lata(s) e o preço total é de R$ {latas * 80}\n')


# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
# arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Qual o tamanho da área a ser pintada? :  "))

litros = area / 6
litros=litros+(litros*0.1)
latas=0
l18=0
l3=0
resto=0
if litros % 18 == 0:
    l18 = litros / 18

else:
    l18 = (litros // 18) + 1

if litros % 3.6 == 0:
    l3 = litros / 3.6

else:
    l3 = (litros // 3.6) + 1


print(f'Serão comprada(s) {int(l18)} lata(s) 18 e o preço total é de R$ {l18 * 80}')
print(f'Serão comprada(s) {int(l3)} lata(s) 3.6 e o preço total é de R$ {l3 * 25}')

if litros>18:
    resto=litros%18
    if resto==0 :
        l18=litros/18
        l3=0
    else:
        l18=(litros//18)
        l3=(resto//3.6 +1)

print(f'Podem ser  comprada(s) {int(l18)} lata(s) 18 l e {int(l3)} latas de 3.6 e o preço total é de R$ {(l3 * 25)+(l18*80)}\n')


# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input("Qual o tamanho da do arquivo em MB? :  "))
velocidade = float(input("Qual a velocidade do link(Mbps):  "))

tempo=arquivo/velocidade
print(f'O tempo de download de um arquivo de {arquivo} MB numa velocidade de {velocidade} Mbps é de: {tempo//60} minuto')