class Hotel:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def get_nome(self):
        return self.nome
    
    def set_nome(self,novo_nome):
        self.nome = novo_nome

    def get_senha(self):
        return self.senha
    
    def set_nome(self,nova_senha):
        self.nome = nova_senha


    def reserva(self):
        quartos = {}
        quarto_reservado = int(input("Digite o quarto desejado: "))
        for i in quartos:
            quartos.append(quarto_reservado)