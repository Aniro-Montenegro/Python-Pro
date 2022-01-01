tpl = (1, 2)
print(type(tpl))

print(dir(tpl))

tpl = tuple(range(10))
print(tpl)

n = (6)
print(n)
print(type(n))

n = (6,)
print(n)
print(type(n))

# desempacotamento

registro =("Aniro", 40)
print(registro)

nome,idade=registro

print(nome)
print(idade)

# função id

registro_1 =("Aniro", 40)
print(registro_1)

registro_2 =("André", 43)
print(registro_2)

registro_3= registro_1+registro_2
print(registro_3)

print(id(registro_1))
print(id(registro_2))
print(id(registro_3))
