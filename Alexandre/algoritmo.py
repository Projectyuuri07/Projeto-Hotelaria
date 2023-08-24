from classe import*
import os
import time

def espera():
    time.sleep(2)

hotel = Hotel(12,6,6)

while True:
    x = 1
    try:
        print("------------------------------------------Bem vindo ao Hotel GP2------------------------------------------")
        escolha = int(input(" [1] Cadastro \n [2] Fazer Login\n [3] Quartos disponiveis\n [4] Sair\n Digite sua escolha:"))
        match escolha:
            case 1:
                os.system("cls")
                cliente = Hotel()
                cliente.cadastro(nome = input("Digite seu nome:"), senha = input("Digite sua senha"))
                self.nome = input("Digite o nome de usuario:")
                self.senha = input("Digite a senha:")


            case 2:
                os.system("cls")
                username = input("Digite o nome de usuario:")
                senha = input("Digite a senha:")

                cliente_logado = None
                for cliente in clientes:
                    if cliente.validar_login(username, senha):
                        cliente_logado = cliente
                        break

            case 3:
                
                
            case 4:
                os.system("cls")
                print("Saindo do sistema...")
                espera()
                break
    except ValueError:
        print("Opção inválida. Digite um número válido.")