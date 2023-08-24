from classess import *
import os
import time

def espera():
    time.sleep(2)

ibis = Hotel(12,6,6)
clientes = []
reservas_cliente = []

while True:
    x = 1
    try:
        print("------------------------------------------\n\nBem vindo ao Hotel GP2\n\n------------------------------------------\n\n")
        escolha = int(input("[1] Cadastro\n[2] Login\n[3] Sair\nSua escolha: "))
        match escolha:
            case 1:
                os.system("cls")
                print("Cadastro iniciado!\n")
                cliente = Cliente(nome=input("Digite seu nome: "), senha=int(input("Digite sua senha: ")))
                print("Cadastrado com sucesso!")
                print (f"{cliente.get_nome()}")
                print (f"{cliente.get_senha()}")
                clientes.append(cliente)
                os.system("pause")
                os.system("cls")
               

            case 2:
                os.system("cls")
                print("Esses são os clientes já cadastrados em nosso sistema:\n")
                for i in clientes:
                    print(i.get_nome())
                nome_login = input("Qual o seu nome: ")
                if nome_login == cliente.get_nome():
                    senha_login = int(input("Digite sua senha: "))
                    if senha_login == cliente.get_senha():
                        print("Login realizado com sucesso! Encaminhando para a sessão de quartos")
                        os.system("pause")
                        os.system("cls")

                        seleção = int(input("Bem-vindo a sessão de quartos!\n\n As categorias disponíveis são: \n[1] Simples \n[2] Casal \n[3] Duplo \n[4] Duplo Casal \n[5] Luxo \n[6] Master\n[7] Exibir reservas \n\nSua escolha: "))
                        match seleção:
                            case 1:
                                print("O quarto simples possui uma cama. com espaço para no máximo 1 pessoa.\n")
                                simples = {"1":"Disponivel", "2":"Disponível"}
                                print(f"Esses são os quartos para a categoria simples: {simples}")
                                reserva = int(input("Qual deseja reservar? \n Sua escolha: "))
                                if reserva == 1:
                                    simples[1, "Disponível"] = 1, "Indisponível"
                                    cliente.reservas_cliente(tipo="Simples", número="Quarto 1")
                                elif reserva == 2:
                                    simples [2, "Disponível"] = 2, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Simples", número="Quarto 2")
                            
                            case 2:
                                casal = {1 : "Disponivel", 2 : "Disponível"}
                                print(f"Esses são os quartos para a categoria simples: {casal}")
                                reserva = int(input("Qual deseja reservar? \n Sua escolha: "))
                                if reserva == 1:
                                    casal[1, "Disponível"] = 1, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Casal", número="Quarto 1")
                                elif reserva == 2:
                                    simples [2, "Disponível"] = 2, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Casal", número="Quarto 2")
                            
                            case 3:
                                duplo = {1 : "Disponivel", 2 : "Disponível"}
                                print(f"Esses são os quartos para a categoria simples: {duplo}")
                                reserva = int(input("Qual deseja reservar? \n Sua escolha: "))
                                if reserva == 1:
                                    duplo[1, "Disponível"] = 1, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Duplo", número="Quarto 1")
                                elif reserva == 2:
                                    duplo [2, "Disponível"] = 2, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Duplo", número="Quarto 2")

                            case 4:
                                duplo_casal = {1 : "Disponivel", 2 : "Disponível"}
                                print(f"Esses são os quartos para a categoria simples: {duplo_casal}")
                                reserva = int(input("Qual deseja reservar? \n Sua escolha: "))
                                if reserva == 1:
                                    duplo_casal[1, "Disponível"] = 1, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Duplo Casal", número="Quarto 1")
                                elif reserva == 2:
                                    duplo_casal[2, "Disponível"] = 2, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Duplo Casal", número="Quarto 2")
                            
                            case 5:
                                luxo = {1:"Disponivel", 2:"Disponível"}
                                print(f"Esses são os quartos para a categoria simples: {luxo}")
                                reserva = int(input("Qual deseja reservar? \n Sua escolha: "))
                                if reserva == 1:
                                    luxo[1] = "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Luxo", número="Quarto 1")
                                elif reserva == 2:
                                    luxo[2] = "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Luxo", número="Quarto 2")
                            
                            case 6:
                                master = {1 : "Disponivel", 2 : "Disponível"}
                                print(f"Esses são os quartos para a categoria simples: {master}")
                                reserva = int(input("Qual deseja reservar? \n Sua escolha: "))
                                if reserva == 1:
                                    master[1, "Disponível"] = 1, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Master", número="Quarto 1")
                                elif reserva == 2:
                                    simples [2, "Disponível"] = 2, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                    cliente.reservas_cliente(tipo="Master", número="Quarto 2")

                            case 7:
                                print(f"Você possuí estes quartos reservados: {cliente.get_tipo()}, sendo eles: {cliente.get_número()}")
                    else:
                        print("Login falhou, senha incorreta.")

    except ValueError:
        print("Opção inválida. Digite um número válido.")
        os.system("pause")
        os.system("cls")