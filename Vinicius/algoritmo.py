from classess import *
import os
import time

def espera():
    time.sleep(2)

ibis = Hotel(12,6,6)
clientes = []

while True:
    x = 1
    try:
        print("------------------------------------------Bem vindo ao Hotel GP2------------------------------------------")
        escolha = int(input("[1] Cadastro\n[2] Login\n[3] Sair\nQuartos\nSua escolha: "))
        match escolha:
            case 1:
                os.system("cls")
                cliente = Cliente(nome=input("Digite seu nome: "), senha=int(input("Digite sua seha: ")))
                print("Cadastrado com sucesso!")
                print (f"{cliente.get_nome()}")
                print (f"{cliente.get_senha()}")
                for cliente in clientes:
                    cliente.append(clientes)

            case 2:
                nome_login = input("Qual o seu nome: ")
                for cliente in clientes:
                    print(f"{clientes}")
                if nome_login in clientes:
                    senha_login = int(input("Digite sua senha: "))
                

                

            case 3:
                os.system("cls")
                print("Saindo do sistema...")
                espera()
                break
    except ValueError:
        print("Opção inválida. Digite um número válido.")