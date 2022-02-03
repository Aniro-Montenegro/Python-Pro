'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''


class Quadrado:
    def __init__(self, tamanho_lado=1):
        self.tamanho_lado = tamanho_lado

    def mudarValor(self, novo_valor):
        self.tamanho_lado = novo_valor

    def retornaValor(self):
        return self.tamanho_lado

    def calculoArea(self):
        return self.tamanho_lado ** 2


if __name__ == '__main__':
    q = Quadrado(tamanho_lado=20)
    print(f'Valor={q.retornaValor()}')
    print(f'Area ={q.calculoArea()}')
    q.mudarValor(50)
    print(f'Valor={q.retornaValor()}')
    print(f'Area ={q.calculoArea()}')
