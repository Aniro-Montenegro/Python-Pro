nome = input('Digite o seu nome: ')
nome_invertido = nome[::-1]
print(nome_invertido.upper())
"""
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente 
utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas 
ou minúsculas.

"""

nome = input('Digite o seu nome: ')
nome_invertido = "".join(reversed(nome.upper()))
print(nome_invertido)

nome = input('Digite o seu nome: ')
lista = nome.split(" ")
nome_invertido = " ".join(reversed(lista))
print(nome_invertido.upper())
