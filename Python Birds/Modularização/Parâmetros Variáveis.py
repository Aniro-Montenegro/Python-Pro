def soma(*args):
    aux = 0
    for valor in args:
        aux += valor
    return aux


print(soma())
print(soma(1))
print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9))


def f(**kwargs):
    print(kwargs)


print(f(nome='Aniro'))

args = (1, 2, 3, 4)
kwargs = {'nome': 'Aniro', 'sobrenome': 'João'}


def funcao(*argus, **kwargus):
    print(argus)
    print(kwargus)


args = (1, 2, 3, 4)
kwargs = {'nome': 'Aniro', 'sobrenome': 'João'}
print(args)
print(kwargs)

print(funcao(args, kwargs))

print(funcao(*args, **kwargs))
