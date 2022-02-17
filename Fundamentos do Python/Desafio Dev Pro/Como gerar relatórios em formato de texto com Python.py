lista_de_dados = []


def transformar_mb(tamanho_em_bytes: str):
    tamanho = int(tamanho_em_bytes) / (2 ** 10) ** 2
    return round(tamanho, 2)


with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_mb((linha[16:]))
        lista_de_dados.append((usuario, tamanho_em_disco))

cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.      Usuário          Espaço utilizado      % do uso

'''

with open('relatorios.txt', 'w', encoding="utf-8") as arquivo:
    tamanho_total_consumido = sum([tamanho for _, tamanho in lista_de_dados])
    arquivo.writelines(cabecalho)
    for indice, dados in enumerate(lista_de_dados, start=1):
        usuario, tamanho_em_disco = dados
        arquivo.writelines(f'{indice:<4}    {usuario}     {tamanho_em_disco:9} MB      '
                           f'{tamanho_em_disco/tamanho_total_consumido:>8.2%}\n')
    arquivo.writelines('\n\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {tamanho_total_consumido/len(lista_de_dados):.2f} MB')

