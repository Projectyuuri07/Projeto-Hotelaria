
class Hotel:
    def __init__(self, nome, endereço):
        self.nome = nome
        self.endereço = endereço

    def login(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
    def adicionar_ap(self, quarto):
        self.quartos.append(quarto)
    
    def listar_aps(self):
        print("Quartos disponíveis no {self.nome}:")
        for quarto in self.quartos:
            print(quarto)

class Quartos(Hotel):
