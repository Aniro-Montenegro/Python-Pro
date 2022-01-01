lista = [1, 2, 3, 4]
print(lista)

print(type(lista))

lista = list(range(10))
print(lista)

lista = list(range(1, 10))
print(lista)

lista = list(range(0, 20, 2))
print(lista)

lista = list(range(20, 0, -2))
print(lista)
print("")
# ordenar lista

lista = list(range(20, -1, -2))
print("Lista não ordenada: " + str(lista))
lista.sort()
print("Lista ordenada: " + str(lista))

# acrescentar numeros a lista

lista.append(100)
print("Lista ordenada: " + str(lista))

# remover ultimo elemento
print("Lista ordenada: " + str(lista))
x = lista.pop()

print(x)
print("Lista ordenada: " + str(lista))

# inserir varios elemento

lista.extend([150, 200])
print("Lista ordenada: " + str(lista))

lista2 = [300, 350]
lista.extend(lista2)
print("Lista ordenada: " + str(lista))

# concatenar lista

lista += [125, 126]
print("Lista ordenada: " + str(lista))

lista *= 3
print("Lista ordenada: " + str(lista))

# string em lista

lista = 'Aniro Montenegro'.split()
print("Lista : " + str(lista))

lista = 'Lista-separada-por-hifen'.split('-')
print("Lista : " + str(lista))
# juntar lista

palavra = ''.join(lista)
print("Palavra : " + palavra)

palavra = ' '.join(lista)
print("Palavra : " + palavra)

palavra = '-'.join(lista)
print("Palavra : " + palavra)

# lista com varios elementos

lista = [1, 2.5, "String", [1, 2, 3]]

print("Lista : " + str(lista))
