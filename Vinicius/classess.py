class Hotel:
    def __init__(self, quantidade_quartos, quartos_disponiveis, quartos_indisponiveis):
        self.quantidade_quartos = quantidade_quartos
        self.quartos_disponiveis = quartos_disponiveis
        self.quartos_indisponiveis = quartos_indisponiveis

    def reserva(self):
        quartos = {}
        if self.quartos_disponiveis > 0:
            quarto_reservado = int(input("Digite o quarto desejado: "))
            for i in range (self.quartos_disponiveis):
                quartos.append(quarto_reservado)
                self.quartos_disponiveis -1
                self.quartos_indisponiveis +1
        else:
            print("Nenhum quarto disponível!")

class Cliente:
    def __init__(self, nome, senha):
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

    def get_tipo(self):
        return self.tipo
    
    def get_número(self):
        return self.número
    
    def set_reserva(self, novo_tipo):
        self.tipo = novo_tipo

    def set_reserva(self, novo_número):
        self.número = novo_número

    def reservas_cliente(self, tipo, número):
        self.tipo = tipo
        self.número = número
        
class Quartos(Hotel):
    def características(self, camas, preço, espaço):
        self.camas = 1
        self.preço = 100
        self.espaço = 1

class Simples_Casal (Quartos):
    def caracteristicas(self, cama_casal, preço, espaço):
        self.cama_casal = 1
        self.preço = 150
        self.espaço = 2

class Duplo (Quartos):
    def caracteristicas(self, camas, preço, espaço):
        self.camas = 2
        self.preço = 300
        self.espaço = 2

class Duplo_Casal (Quartos):
    def caracteristicas(self, cama_casal, preço, espaço):
        self.camas_casal = 2
        self.preço = 350
        self.espaço = 4

class Luxo (Quartos):
    def caracteristicas(self, cama_luxo, preço, espaço, banheira):
        self.cama_luxo = 1
        self.preço = 450
        self.espaço = 1
        self.banheira = 1

class Master (Quartos):
    def caracteristicas(self, cama_luxo_casal, preço, espaço, banheira, hidromassagem):
        self.cama_luxo_casal = 2
        self.preço = 600
        self.espaço = 2
        self.banheira = 1
        self.hidromassagem = 1