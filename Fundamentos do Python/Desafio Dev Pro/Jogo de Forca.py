palavra_secreta = input('Digite a palavra secreta: ')
palavra_secreta = palavra_secreta.upper()
tamanho_palavra = len(palavra_secreta)
quantidade_erros = 6
palavra_visivel = '_' * tamanho_palavra
lista_visivel=list(palavra_visivel)
while quantidade_erros > 0:
    print(f'Resultado: {palavra_visivel}')
    letra = input('Digite uma letra: ')
    letra=letra.upper()
    if letra in palavra_secreta:
        i = 0
        while i < tamanho_palavra:
            if palavra_secreta[i] == letra:
                lista_visivel[i] = letra
                palavra_visivel="".join(lista_visivel)
            i += 1
        if '_' not in palavra_visivel:
            print('Ganhou!!!')
            quantidade_erros=0
    else:
        quantidade_erros -= 1
        print(f'Você cometeu {6 - quantidade_erros}°')
        print('Perdeu!!!')

