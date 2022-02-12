import os

clearConsole = lambda: print('\n' * 150)

palavra = input('Digite uma palavra a ser descoberta: ').upper()
clearConsole()

print('Jogo da forca')
print('Descubra a palavra')

print('A palavra é: ', end='')
for letra in palavra:
    print('_ ', end='')

conjunto_letras_palavras = set(palavra)
conjunto_letras_digitadas = set()

erros = 0

while not conjunto_letras_palavras.issubset(conjunto_letras_digitadas) and erros < 6:
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)

    if letra_digitada in conjunto_letras_palavras:
        print('A palavra é: ', end='')
        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print('_ ', end='')
    else:
        print()
        erros += 1
        print(f'Você errou {erros} veze(s)')
        print()
    print(f'Letras já escolhidas {conjunto_letras_digitadas}')

if erros >= 6:
    print('Você perdeu')
else:
    print(f'A palavra secreta é {palavra} .Você ganhou')
