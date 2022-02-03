"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos: tipoCombustivel. valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
*abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
foi colocada no veículo
*abastecerPorLitro( ) – método onde é informado
a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
*alterarValor( ) – altera o valor do litro do combustível.
*alterarCombustivel( ) – altera o tipo do combustível.
*alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a
quantidade de combustível total na bomba. """


class BombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel
        self.valorLitro = valorLitro
        self.tipoCombustivel = tipoCombustivel

    def abastecerPorValor(self, valor: float):
        litros = valor / self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - litros)
        print(f"Foram abastecidos {litros:.2f} de {self.tipoCombustivel} com o valor de R${valor:.2f}")
        return litros

    def abastecerPorLitro(self, litro):
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - litro)
        valor = litro * self.valorLitro
        print(f"Foram abastecidos {litro:.2f} de {self.tipoCombustivel} no valor de R${valor:.2f}")
        return valor

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, quantidade_combustivel):
        self.quantidadeCombustivel = quantidade_combustivel.__round__(2)


bomba = BombaCombustível('Gasolina', 3.5, 1000)

print(f'O tipo de combustível é {bomba.tipoCombustivel} , o valor do litro é {bomba.valorLitro} por litro e a '
      f'quantidade na bomba é de {bomba.quantidadeCombustivel} litros')

bomba.abastecerPorLitro(50)
bomba.abastecerPorValor(100)
bomba.alterarValor(2)
bomba.alterarCombustivel("Diesel")
bomba.abastecerPorLitro(50)
bomba.abastecerPorValor(100)

print(f'O tipo de combustível é {bomba.tipoCombustivel} , o valor do litro é {bomba.valorLitro} por litro e a '
      f'quantidade na bomba é de {bomba.quantidadeCombustivel} litros')