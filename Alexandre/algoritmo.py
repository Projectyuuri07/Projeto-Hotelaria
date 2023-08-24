from classe import*
import os


clientes = []
quartos = []

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