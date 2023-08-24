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
    
    


