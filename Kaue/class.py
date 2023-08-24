
class Hotel:
    def __init__(self, nome, endereço):
        self.nome = nome
        self.endereço = endereço
        self.quartos = []

    def adicionar_ap(self, quarto):
        self.quartos.append(quarto)
        