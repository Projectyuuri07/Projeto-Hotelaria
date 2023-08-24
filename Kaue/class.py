
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
    def __init__(self, pessoas, camas, preço):
        self.pessoas = pessoas
        self.camas = camas
        self.preço = preço

class APLuxo(Quartos):
    def __init__(self):
        self.pessoas = 6
        self.camas = 3
        self.preço = 1700

class APMaster(Quartos):
        def __init__(self):
            self.pessoas = 5
            self.camas = 3
            self.preço = 1500

class APSimples(Quartos):
        
        def __init__(self):
            self.pessoas = 1
            self.camas = 1
            self.preço = 900

class APSimplesCasal(Quartos):
       
        def __init__(self):
            self.pessoas = 2
            self.camas = 1
            self.preço = 1000

class APSimplesDuplo(Quartos):
       
        def __init__(self):
            self.pessoas = 2
            self.camas = 2
            self.preço = 1050

class APDuploCasal(Quartos):
        def __init__(self):
            self.pessoas = 4
            self.camas = 2
            self.preço = 1300