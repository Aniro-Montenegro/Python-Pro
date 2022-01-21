lista = [1, 2, 3]
print(lista)
print(type(lista))

lista = list(range(10))
print(lista)

lista = list(range(1, 10))
print(lista)

lista = list(range(0, 100, 2))
print(lista)

lista = list(range(50, 0, -2))
print(lista)

print(dir(lista))

lista.sort()
print(lista)

lista.append(1000)

print(lista)

lista.pop()
print(lista)

lista.extend([15, 25, 32])
print(lista)

lista = lista + [45, 69, 89]
print(lista)

print(lista.__contains__(89))

print(lista * 3)

string = "Aniro Montenegro"

lista = string.split()

print(lista)

string = " ".join(lista)

print(string)

lista = [1, 4.5, "palavra", [5, 6, 3]]

print(lista)
