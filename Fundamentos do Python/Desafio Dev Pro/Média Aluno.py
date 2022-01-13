primeira_nota = int(input('Digite a primeira nota: '))
segunda_nota = int(input('Digite a segunda nota: '))
media_aluno = (primeira_nota + segunda_nota) / 2
if 7 <= media_aluno < 10:
    print("Aprovado")
elif media_aluno< 7:
    print('Reprovado')
else:
    print('Aprovado com louvor')
