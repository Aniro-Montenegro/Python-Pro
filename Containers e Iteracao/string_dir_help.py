palavra = 'Aniro'
print(type(palavra))
print(palavra)
print("")

palavra = "João"
print(type(palavra))
print(palavra)
print("")

palavra1 = "'José'"
print(type(palavra1))
print(palavra1)
print("")

palavra2 = '"Maria"'
print(type(palavra2))
print(palavra2)
print("")

palavra = 'Aniro \nMontenegro'
print(type(palavra))
print(palavra)
print("")

palavra = '''Aniro Montenegro 
Rua Dois'''
print(type(palavra))
print(palavra)
print("")

palavra = ''''"Aniro"'''''
print(type(palavra))
print(palavra)
print("")

concatenacao = palavra1 + palavra2
print(type(concatenacao))
print(concatenacao)
print("")

concatenacao = palavra1 * 2
print(type(concatenacao))
print(concatenacao)
print("")

# dir

print(dir(''))
print("")

# help

help("Aniro".lower)
