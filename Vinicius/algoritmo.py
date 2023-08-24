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
        escolha = int(input("[1] Cadastro\n[2] Login\n[3] Sair\n[4] Quartos\nSua escolha: "))
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
                        escolha = 3
                    
                    else:
                        print("Login falhou, senha incorreta.")
                
            case 3:
                print("Bem-vindo a sessão de quartos!\n\n As categorias disponíveis são: \n [1] Simples \n[2] Casal \n[3] Duplo \n[4] Duplo Casal \n[5] Luxo \n[6] Master \n\n Sua escolha: ")

    except ValueError:
        print("Opção inválida. Digite um número válido.")
        os.system("pause")
        os.system("cls")