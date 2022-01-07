# Fundamento de Lógica de programação.


# Tipo Inteiro

x = 1
print("O valor 1 é do tipo " + str(type(x)))

# Operações

n = 1 + 1  # soma
print(n)

n = 1 - 1  # subtração
print(n)

n = 2 * 2  # multiplicação
print(n)

n = 2 / 2  # divisão
print(n)

n = 2 / 4  # divisão
print(n)

n = 50 % 2  # resto da divisao
print(n)

n = 45 // 2  # divisao inteira
print(n)

n = 7 ** 3  # exponenciação
print(n)

n = 2 ** 63 - 1  # exponenciação
print(n)

n = 2 ** 1000  # exponenciação
print(n)

n = 1_252_569_256
print(n)

# Ponto flutuante

n = 7.1563
print(type(n))

print(10.5 + 2, 7.3 - 3.2, 4.5 / 2.3, 4.6 * 5, 4.5 ** 3, 7.5 // 2)

# Variaveis . Nomes que representam um valor ou objeto

pi = 3.14

print(pi)

raio = 2

print(pi * (raio ** 2))

# Cadeia de caracteres ou string

p = 'Palavra'
print(p)

print(p[0:3])

p = "'Entre aspas simples"
print(p)

p = '"Entre aspas duplas"'
print(p)

p = "'''Entre aspas triplas'''"
print(p)

p = '"""Entre aspas triplas"""'
print(p)

p = '''Pulando 
linha em Python'''

print(p)

# Tipos Booleanos  True e False

b = True
f = False
print(type(b))

print(not b)

print(not f)

print(b and f)

print(b and b)

print(f and f)

print(b or f)

print(b or b)

print(f or f)

e = 5 < 6

print(e)

e = 5 <= 6

print(e)

e = 5 > 6

print(e)

e = 5 >= 6

print(e)

e = 5 == 6

print(e)

p = 'Aniro'
v = 'Marisa'

print(p == v)

p = 'Aniro'
v = 'aniro'

print(p == v)

p = 'Aniro'
v = 'Aniro'

print(p == v)

# Desvios Logicos

idade = 67

if 18 <= idade < 65:
    print(f'Maior de idade: {idade}')
elif idade >= 65:
    print(f'Pessoa idosa: {idade}')
else:
    print(f'Menor de idade: {idade}')


# Funções


def classificar(idade, nome):
    if 18 <= idade < 65:
        return f'{nome} maior de idade: {idade}'
    elif idade >= 65:
        return f'{nome} é uma pessoa idosa: {idade}'
    else:
        return f'{nome} é menor de idade: {idade}'


print(classificar(75, "Aniro"))

# Sequencias

lista = [1, 4.5, "Olá", ['a', 'b', 'c'], (1, "10")]
print(type(lista), lista)

print(lista[0])  ## acessando primeiro elemento

tamanho = len(lista)
print(tamanho)

print(lista[-1])  # acessando o ultimo elemento
print(lista[-2])

# fatiamento

fatia = lista[0:2]
print(fatia)

fatia = lista[:2]
print(fatia)

fatia = lista[2:len(lista)]  # dois ultimos elementos
print(fatia)

fatia = lista[2:]  # dois ultimos elementos
print(fatia)

copia = lista[:]
print(copia)

numeros = list(range(1, 11))
print(numeros)

fatiamento = numeros[0:7:2]  # faz uma fatia da lista pulando de dois em dois
print(fatiamento)

numeros = list(range(0, 100, 3))  # cria uma lista de 0 a 99 pulando de tres em tres
print(numeros)

palavra = 'Aniro Montenegro'

fatia = palavra[0:7]
print(fatia)

# Adição e remoçãod e elementos

print(dir(numeros))

print(numeros.pop)

print(help(numeros.pop))

print(numeros.pop())

print(numeros)
numeros.append(150)
print(numeros)

numeros.extend([159, 450])  # concatenacao de listas
print(numeros)

l = [1, 2, 3, 4] + [5, 6, 7, 8, 9]
print(l)

s = [1, 3] * 4
print(s)

st = "Aniro " + "Montenegro"
print(st)

st = ("Aniro " + "Montenegro ") * 3
print(st)

# Lacos de repetição

idades = [18, 43, 75, 12]

for idade in idades:
    print(classificar(idade, "Aniro"))

# Dicionario

linguas = {'pt': 'Portugues', 'en': 'Ingles'}
print(linguas)
print(linguas.values())

print(linguas['pt'])

linguas['es'] = 'Espanhol'
print(linguas)
print(linguas.values())

print(linguas['es'])

for chave in linguas:
    print(chave)

for chave in linguas.keys():
    print(chave)

for value in linguas.values():
    print(value)

for chave, valor in linguas.items():
    print(chave, valor)
