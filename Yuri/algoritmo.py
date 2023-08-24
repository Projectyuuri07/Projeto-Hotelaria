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

        match opcao:
            case 1:
                limpar()
                hotel.listar_Quartos()
                print("Quartos listados com sucesso!")
                parar()
            case 2:
                limpar()
                nome = input("Digite o nome do hóspede: ")
                cpf = input("Digite o CPF do hóspede: ")
                data_entrada = input("Digite a data de entrada (dd/mm/aaaa): ")
                data_saida = input("Digite a data de saída (dd/mm/aaaa): ")
                reserva = Reserva(nome, cpf, data_entrada, data_saida)
                numero_quarto = input("Digite o número do quarto que deseja reservar: ")
                for quarto in hotel.quartos:
                    if quarto.numero == numero_quarto:
                        quarto.add_reserva(reserva)
                        hotel.reservas.append(reserva)
                        print("Reserva feita com sucesso!")
                        parar()
                        break
                else:
                    print("Quarto não encontrado.")
            case 3:
                limpar()
                hotel.listar_Reservas()
                print("Reservas listadas com sucesso!")
                parar()
            case 4:
                break
            case _:
                print("Opção inválida.")