from classes import *
import os
import time

def espera():
    time.sleep(2)

hotel = Hotel(12,6,6)
clientes = []

while True:
    x = 1
    try:
        print("------------------------------------------Bem vindo ao Hotel GP2------------------------------------------")
        escolha = int(input("[1] Cadastro\n[2] Login\n[3] Sair\nQuartos\nSua escolha: "))
        match escolha:
            case 1:
                os.system("cls")
                cliente = Hotel()
                cliente.cadastro(nome=input("Digite seu nome: "), senha = input("Digite sua senha: "))
                print("Cadastrado com sucesso!")
                print (f[cliente.get_nome()])
                print (f[cliente.get_senha()])
                for cliente in clientes:
                    cliente.append(clientes)

            case 2:
                

            case 3:
                os.system("cls")
                print("Saindo do sistema...")
                espera()
                break
    except ValueError:
        print("Opção inválida. Digite um número válido.")