import math

area_a_ser_pintada = int(input("Digite os metros quadrados a serem pintados"))  # area em metros quadrados
area_com_folga = area_a_ser_pintada * 1.1
litros_por_metros = 6
litros_a_serem_usados = area_com_folga / litros_por_metros
litros_por_lata = 18
numero_latas = math.ceil(litros_a_serem_usados / litros_por_lata)  # arredonda para cima
valor_latas = numero_latas * 80
print(f'Você deverá usar {numero_latas} latas no valor de R$ {valor_latas} ')
litros_por_galao = 3.6
numero_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
valor_galoes = numero_galoes * 25
print(f'Você deverá usar {numero_galoes} no valor de R$ {valor_galoes} ')

# Compra de tinta otimizada por valor

numero_latas = math.floor(litros_a_serem_usados / litros_por_lata)  # arredonda para baixo
valor_de_latas = numero_latas * 80
litros_faltantes = litros_a_serem_usados % litros_por_lata
numero_galoes=math.ceil(litros_faltantes/litros_por_galao)
valor_com_galoes = numero_galoes * 25
valor_total = valor_com_galoes + valor_de_latas

print(f'Você deverá usar {numero_latas} latas de 18 litros mais {numero_galoes} galoes no valor de R$ {valor_total}  ')
