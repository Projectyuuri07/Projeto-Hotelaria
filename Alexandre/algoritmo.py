from classe import*
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
        escolha = int(input(" [1] Cadastro \n [2] Fazer Login\n [3] Quartos disponiveis\n [4] Sair\n Digite sua escolha:"))
        match escolha:
            case 1:
                os.system("cls")
                cliente = Cliente(nome=input("Digite seu nome: "), senha =("Digite sua seha: "))
                print("Cadastrado com sucesso!")
                print (f"{cliente.get_nome()}")
                print (f"{cliente.get_senha()}")
                for cliente in clientes:
                    cliente.append(clientes)

            case 2:
                os.system("cls")
                username = input("Digite o nome de usuario:")
                senha = input("Digite a senha:")

                cliente_logado = None
                for cliente in clientes:
                    if cliente.validar_login(username, senha):
                        cliente_logado = cliente
                        break
                
            case 4:
                os.system("cls")
                print("Saindo do sistema...")
                espera()
                break
    except ValueError:
        print("Opção inválida. Digite um número válido.")