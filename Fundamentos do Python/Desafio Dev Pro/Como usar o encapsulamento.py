"""
Classe Pessoa: Crie uma classe que modele uma pessoa: Atributos: nome, idade, peso e altura Métodos: Envelhecer,
engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21
anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.nome = nome

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            otavio.crescer()

    def crescer(self):
        self.altura += 0.5

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso


otavio = Pessoa('Otavio', 2, 12, 100)

for _ in range(22):
    otavio.envelhecer()
    print(f'A idade de {otavio.nome} = {otavio.idade} e sua altura é {otavio.altura}')
