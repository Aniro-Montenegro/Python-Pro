# Duas constantes True e False(Verdadeiro e Falso)

x = True
y = False
z = True
w = False

print(type(x))
print("")
# Operacões basicas

# Negação

print("not True= " + str(not x))
print("not False= " + str(not y))
print("")
# OU

print("True or False = " + str(x or y))
print("True or True = " + str(x or z))
print("False or False = " + str(w or y))
print("False or True = " + str(y or x))

print("")
# and

print("True and False = " + str(x and y))
print("True and True = " + str(x and z))
print("False and False = " + str(w and y))
print("False and True = " + str(y and x))
print("")

# Expressões boleanas


print("3 > 5 = " + str(3 > 5))
print("3>=5 = " + str(3 >= 5))
print("3 < 5 = " + str(3 < 5))
print("3<=5 = " + str(3 <= 5))
print("3==5 = " + str(3 == 5))
print("3!=5 = " + str(3 != 5))
print("")

# Intervalo

n = 5
print("n = 5")
print("n < 10 and n > 4 =" + str(n < 10 and n > 4))

n = 5
print("n = 5")
print("10 > n > 4 =" + str(10 > n > 4))
