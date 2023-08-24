from classes import*
import os

def limpar():
    os.system('cls')

def parar():
    os.system('pause')

def main():
    limpar()
    hotel = Hotel ("Meu Hotel")
    while True:
        limpar()
        print("Meu Hotel\n 1. Listar Quartos\n 2. Fazer Reserva\n 3. Listar Reservas\n 4. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número.")
            continue

        