saque = 575

notas_100 = notas_50 = notas_10 = notas_5 = notas_1 = 0

notas_100, saque = divmod(saque, 100)
notas_50, saque = divmod(saque, 50)
notas_10, saque = divmod(saque, 10)
notas_5, saque = divmod(saque, 5)
notas_1, saque = divmod(saque, 1)

if notas_100 > 0:
    print(f'{notas_100} nota(s) de 100')
if notas_50 > 0:
    print(f'{notas_50} nota(s) de 50')
if notas_10 > 0:
    print(f'{notas_10} nota(s) de 10')
if notas_5 > 0:
    print(f'{notas_5} nota(s) de 5')
if notas_1 > 0:
    print(f'{notas_1} nota(s) de 1')
