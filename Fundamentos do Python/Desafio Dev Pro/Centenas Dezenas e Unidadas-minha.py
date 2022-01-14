numero = 320
centenas_str = dezenas_str = unidades_str = ""

centenas_int = numero // 100

if centenas_int == 1:
    centenas_str = '1 centena '
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centenas'


dezenas_int = (numero-centenas_int*100)//10

if dezenas_int == 1:
    dezenas_str = '1 dezena '
elif dezenas_int > 1:
    dezenas_str = f'{dezenas_int} dezenas'

unidades_int = (numero-centenas_int*100)-(dezenas_int*10)


if unidades_int == 1:
    unidades_str = '1 unidade '
elif unidades_int > 1:
    unidades_str = f'{unidades_int} unidades'




print(centenas_str, dezenas_str, unidades_str)

