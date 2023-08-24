import os

class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.quartos = []
        self.reservas = []
    
    def add_quarto(self, quarto):
        self.quartos.append(quarto)

    def listar_Quartos(self):
        for quarto in self.quartos:
            print(quarto)

    def listar_Reservas(self):
        for reserva in self.reservas:
            print(reserva)
    
    def add_reserva(self, reserva):
        self.reservas.append(reserva)
    
    
class Quartos:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.reservas = []

class Reserva:
    def __init__(self, nome, cpf, data_entrada, data_saida):
        self.nome = nome
        self.cpf = cpf
        self.data_entrada = data_entrada
        self.data_saida = data_saida

    def __str__(self):
        return input(f'Nome: {self.nome}\nCPF: {self.cpf}\nData de entrada: {self.data_entrada}\nData de saída: {self.data_saida}')    

class AP_Luxo(Quartos):
    def __init__(self, numero, tipo, preco):
        super().__init__(numero, tipo, preco)
        self.tipo = 'Apartamento de Luxo'
        self.preco = 500

class AP_MAster(Quartos):
    def __init__(self, numero, tipo, preco):
        super().__init__(numero, tipo, preco)
        self.tipo = 'Apartamento Master'
        self.preco = 300

class AP_Simples(Quartos):
    def __init__(self, numero, tipo, preco):
        super().__init__(numero, tipo, preco)
        self.tipo = 'Apartamento Simples'
        self.preco = 150

class AP_SimplesCasal(Quartos):
    def __init__(self, numero, tipo, preco):
        super().__init__(numero, tipo, preco)
        self.tipo = 'Apartamento Simples Casal'
        self.preco = 200

class AP_Duplo(Quartos):
    def __init__(self, numero, tipo, preco):
        super().__init__(numero, tipo, preco)
        self.tipo = 'Apartamento Duplo'
        self.preco = 250

class AP_DuploCasal(Quartos):
    def __init__(self, numero, tipo, preco):
        super().__init__(numero, tipo, preco)
        self.tipo = 'Apartamento Duplo Casal'
        self.preco = 300


