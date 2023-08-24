from classes import *
import os
import time

def espera():
    time.sleep(2)

ibis = Hotel('Ibis')
clientes = []

def main():
    while True:
        x = 1
        try:
            print("Bem vindo ao Hotel")
            escolha = int(input(" [1]-Cadastro\n [2]-Login\n [3]-Sair\nSua escolha: "))
            if escolha == 1:
                os.system("cls")
                cliente = Cliente(nome=input("Digite seu nome: "), senha=int(input("Digite sua senha: ")))
                print("Cadastrado com sucesso!")
                print (f"{cliente.get_nome()}")
                print (f"{cliente.get_senha()}")
                clientes.append(cliente)
                os.system("pause")
                os.system("cls")

            elif escolha == 2:
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

                        seleção = int(input("Bem-vindo a sessão de quartos!\n\n As categorias disponíveis de quartos são: \n [1]-Simples \n[2]-Casal \n[3]-Duplo \n[4]-Duplo Casal \n[5]-Luxo \n[6]-Master \n\nSua escolha: "))
                        if seleção == 1:
                            simples = {1 : "Disponivel", 2 : "Disponível"}
                            print(f"Esses são os quartos para a categoria simples: {simples}")
                            reserva = int(input("Qual deseja reservar? \n Sua escolha: "))
                            if reserva in simples.keys():
                                simples[reserva] = "Indisponível"
                                print("Reserva realizada com sucesso!")
                            else:
                                print("Quarto não disponível.")
                    else:
                        print("Login falhou, senha incorreta.")
            elif escolha == 3:
                break
            else:
                print("Opção inválida. Digite um número válido.")
        except ValueError:
            print("Opção inválida. Digite um número válido.")
            os.system("pause")
            os.system("cls")
