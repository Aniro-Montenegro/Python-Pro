'''
Faça um programa que leia 5 números e informe o maior número.
'''

lista=[]
while len(lista)<5:
    lista.append(int(input("Digite um número inteiro")))
maior=0
for n in lista:
    if n>=maior:
        maior=n
print(f'O maior número da lista é o {maior}')