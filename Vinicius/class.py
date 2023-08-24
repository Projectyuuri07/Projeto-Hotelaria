class Hotel:
    def __init__(self, quantidade_quartos, quartos_disponiveis):
        self.quantidade_quartos = quantidade_quartos
        self.quartos_disponiveis = quartos_disponiveis

    def cadastro(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_senha(self):
        return self.senha
    
    def set_nome(self, nova_senha):
        self.nome = nova_senha


    def reserva(self):
        quartos = {}
        if self.quartos_disponiveis > 0:
            quarto_reservado = int(input("Digite o quarto desejado: "))
            for i in range (self.quartos_disponiveis):
                quartos.append(quarto_reservado)
                self.quartos_disponiveis -1
        else:
            print("Nenhum quarto disponível!")