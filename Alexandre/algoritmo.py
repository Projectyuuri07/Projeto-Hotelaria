from classe import *
import os
import time

def espera():
    time.sleep(2)

ibis = Hotel(12,6,6)
clientes = []

while True:
    try:
        print("------------------------------------------Bem vindo ao Hotel GP2------------------------------------------")
        escolha = int(input("[1] Cadastro\n[2] Login\n[3] Sair\nSua escolha: "))
        match escolha:
            case 1:
                os.system("cls")
                cliente = Cliente(nome=input("Digite seu nome: "), senha=int(input("Digite sua senha: ")))
                print("Cadastrado com sucesso!")
                print (f"{cliente.get_nome()}")
                print (f"{cliente.get_senha()}")
                clientes.append(cliente)
                os.system("pause")
                os.system("cls")
               

            case 2:
                os.system("cls")
                for i in clientes:
                    print(i.get_nome())
                nome_login = input("Qual o seu nome: ")
                if nome_login == cliente.get_nome():
                    senha_login = int(input("Digite sua senha: "))
                    if senha_login == cliente.get_senha():
                        print("Login realizado com sucesso! Encaminhando para a sessão de quartos")
                        os.system("pause")
                        os.system("cls")

                        seleção = int(input("Bem-vindo a sessão de quartos!\n\n As categorias disponíveis são: \n [1] Simples \n[2] Casal \n[3] Duplo \n[4] Duplo Casal \n[5] Luxo \n[6] Master \n\n Sua escolha: "))
                        match seleção:
                            case 1:
                                simples = {1 : "Disponivel", 2 : "Disponível"}
                                print(f"Esses são os quartos para a categoria simples: {simples}")
                                reserva = int(input("Qual deseja reservar? \n Sua escolha: "))
                                if reserva == 1:
                                    simples[1, "Disponível"] = 1, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                elif reserva == 2:
                                    simples [2, "Disponível"] = 2, "Indisponível"
                                    print("Reserva realizada com sucesso!")
                                
                    else:
                        print("Login falhou, senha incorreta.")

                    
            case 3:
                os.system("cls")
                print("Obrigado pela preferencia!")
                espera()
                print("Saindo...")
                espera()
                break

    except ValueError:
        print("Opção inválida. Digite um número válido.")
        os.system("pause")
        os.system("cls")