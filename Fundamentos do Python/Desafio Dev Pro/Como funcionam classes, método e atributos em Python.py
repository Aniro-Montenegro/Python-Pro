class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    """
        FUNÇÃO QUE RETORNA A COR
        cor : return
    """
    def mostra_cor(self):
        return self.cor


circulo_primeiro = CirculoPerfeito()

circulo_segundo = CirculoPerfeito()

print(id(circulo_primeiro), id(circulo_segundo))

print(circulo_primeiro.mostra_cor(),circulo_segundo.mostra_cor())
circulo_segundo.cor='Amarelo'
print(circulo_primeiro.mostra_cor(),circulo_segundo.mostra_cor())
