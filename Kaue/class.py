
class Hotel:
    def __init__(self, nome, endereço):
        self.nome = nome
        self.endereço = endereço
        self.quartos = []

    def adicionar_ap(self, quarto):
        self.quartos.append(quarto)
    
    def listar_aps(self):
        print("Quartos disponíveis no {self.nome}:")
        for quarto in self.quartos:
            print (quarto)