import os 

class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.hospedes = []
        self.quartos = []
        self.reservas = []
    
    def add_hospede(self, hospede):
        self.hospedes.append(hospede)

    def add_reserva(self, reserva):
        self.reservas.append(reserva)
        print("Reserva adicionada")

    #definir um limite de 2 quartos para cada tipo
    def add_quarto(self, quarto):
        self.quartos.append(quarto)
        print("Quarto adicionado")

    def get_reservas(self):
        return self.reservas
        
    def get_hospede(self):
        return self.hospedes
    
    def set_hospede(self):
        pass

    def add_quarto(self, quarto):
        self.quartos.append(quarto)

    def get_quarto(self):
        return self.quartos

class Quartos(Hotel):
    def __init__(self, tipo, numero, preco):
        self.tipo = tipo
        self.numero = numero
        self.preco = preco

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero

    def get_preco(self):
        return self.preco

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_numero(self, numero):
        self.numero = numero
 
    def set_preco(self, preco):
        self.preco = preco

class AP_Luxo(Quartos):
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco
        self.tipo = "AP_Luxo"

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero

    def get_preco(self):
        return self.preco

class AP_Master(Quartos):
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco
        self.tipo = "AP_Master"

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero

    def get_preco(self):
        return self.preco

class AP_Simples(Quartos):
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco
        self.tipo = "AP_Simples"

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero

    def get_preco(self):
        return self.preco

class AP_SimplesCasal(Quartos):
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco
        self.tipo = "AP_SimplesCasal"

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero

    def get_preco(self):
        return self.preco

class AP_Duplo(Quartos):
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco
        self.tipo = "AP_Duplo"

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero

    def get_preco(self):
        return self.preco

class AP_DuploCasal(Quartos):
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco
        self.tipo = "AP_DuploCasal"

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero

    def get_preco(self):
        return self.preco
