s1 = input('Digite uma palavra: ')
s2 = input('Digite outra palavra: ')
print(f'Tamanho da String 1 : {s1} = {len(s1)} caracteres')
print(f'Tamanho da String 2 : {s2} = {len(s2)} caracteres')
comparacao_tamanho = 'diferentes'
comparacao_conteudo = 'diferente'
if s1 == s2:
    comparacao_tamanho = 'iguais'
    comparacao_conteudo = 'igual'
elif len(s1) == len(s2):
    comparacao_tamanho = 'iguais'
print(f'As duas string são de tamanho {comparacao_tamanho}')
print(f'As duas string são de conteudo {comparacao_conteudo}')
