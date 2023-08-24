from classe import*
import os
import time

def espera():
    time.sleep(2)

clientes = []
quartos_disponiveis = []

hotel = Hotel(len(quartos_disponiveis), quartos_disponiveis, 0)
while True:
    x = 1
    try:
        print("------------------------------------------Bem vindo ao Hotel GP2------------------------------------------")
        escolha = int(input(" [1] Fazer Login\n [2] Quartos disponiveis\n [3] Sair\n Digite sua escolha:"))
        match escolha:
            case 1:
                os.system("cls")
                username = input("Digite o nome de usuario:")
                senha = input("Digite a senha:")

                cliente_logado = None
                for cliente in clientes:
                    if cliente.validar_login(username, senha):
                        cliente_logado = cliente
                        break

            case 2:
                

            case 3:
                os.system("cls")
                print("Saindo do sistema...")
                espera()
                break
    except ValueError:
        print("Opção inválida. Digite um número válido.")