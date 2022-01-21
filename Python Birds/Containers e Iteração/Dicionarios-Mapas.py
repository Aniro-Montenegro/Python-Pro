linguas = {'br': 'portugues', 'en': 'ingles'}
print(linguas)

print(linguas['br'])

print(linguas.get('br'))

print(linguas.get('brs', 'não definida'))

s = 'br' in linguas

print(s)

linguas['es'] = 'espanho'

print(linguas['es'])

linguas['es'] = 'espanhol'

print(linguas['es'])

for chave in linguas:
    print(chave)

for chave in linguas.keys():
    print(chave)

for valores in linguas.values():
    print(valores)

for chave, valor in linguas.items():
    print(chave, valor)

linguas.pop('br')
print(linguas.values())

del linguas['es']
print(linguas.values())

