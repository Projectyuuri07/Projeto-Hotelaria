class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.quartos = [AP_Luxo(i) for i in range(1, 3)] + [AP_Master(i) for i in range(3, 5)] + [AP_Simples(i) for i in range(5, 7)] + [AP_SimplesCasal(i) for i in range(7, 9)] + [AP_Duplo(i) for i in range(9, 11)] + [AP_DuploCasal(i) for i in range(11, 13)] 
        self.reservas = []
    
    def listar_Quartos(self):
        for quarto in self.quartos:
            print(quarto)

    def listar_Reservas(self):
        for reserva in self.reservas:
            print(reserva)
    
class Quartos:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.reservas = []

    def __str__(self):
        return f'Número: {self.numero}\nTipo: {self.tipo}\nPreço: {self.preco}'

    def add_reserva(self, reserva):
        self.reservas.append(reserva)    

class Reserva:
    def __init__(self, nome, cpf, data_entrada, data_saida):
        self.nome = nome
        self.cpf = cpf
        self.data_entrada = data_entrada
        self.data_saida = data_saida

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nData de entrada: {self.data_entrada}\nData de saída: {self.data_saida}'

class AP_Luxo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, 'Apartamento de Luxo', 500)

class AP_Master(Quartos):
    def __init__(self, numero):
        super().__init__(numero, 'Apartamento Master', 300)

class AP_Simples(Quartos):
    def __init__(self, numero):
        super().__init__(numero, 'Apartamento Simples', 150)

class AP_SimplesCasal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, 'Apartamento Simples Casal', 200)

class AP_Duplo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, 'Apartamento Duplo', 250)

class AP_DuploCasal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, 'Apartamento Duplo Casal', 300)

Hotel.TIPOS_QUARTO = {
    'Luxo': AP_Luxo,
    'Master': AP_Master,
    'Simples': AP_Simples,
    'SimplesCasal': AP_SimplesCasal,
    'Duplo': AP_Duplo,
    'DuploCasal': AP_DuploCasal
    }
    