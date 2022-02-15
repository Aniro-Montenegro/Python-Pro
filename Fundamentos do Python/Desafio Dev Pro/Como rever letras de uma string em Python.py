s = 'Fulano'
tamanho = len(s)

for _ in range(tamanho):
    print(s[0:tamanho])
    tamanho -= 1

s = 'Siclano'
tamanho = len(s)

while s != '':
    print(s)
    s = s[:-1]
