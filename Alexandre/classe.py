class Hotel:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
    
    def reserva(self):
        quartos = []
        quarto_reservado = int(input("Digite o quarto desejado: "))
        for i in quartos:
            quartos.append(quarto_reservado)