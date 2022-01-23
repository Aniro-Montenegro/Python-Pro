def ola(nome):
    return f'Olá {nome}'


print(ola('Aniro'))
print(ola('João'))


def ola(nome, sobrenome):
    return f'Olá {nome} {sobrenome}'


print(ola('Aniro', 'Montenegro'))
print(ola('João', 'Silva'))


def ola(nome, sobrenome='Montenegro'):
    return f'Olá {nome} {sobrenome}'


print(ola('Aniro', 'Montenegro'))
print(ola('João', ))

print(ola(nome='Jose', sobrenome='dos Santos'))

print(ola(sobrenome='dos Santos', nome='José'))
