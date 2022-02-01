s1 = input('Digite uma palavra: ')
s2 = input('Digite outra palavra: ')
print(f'Tamanho da String 1 : {s1} = {len(s1)} caracteres')
print(f'Tamanho da String 2 : {s2} = {len(s2)} caracteres')
if len(s1) != len(s2):
    print('As duas string são de tamanho diferentes')
else:
    print('As duas string são de tamanho iguais')
if s1 == s2:
    print('As duas string são identicas')
else:
    print('As duas string são diferentes')

