from classe import*

while True:
    x = 1
    try:
        print("------------------------------------------Bem vindo ao Hotel GP2------------------------------------------")
        escolha = int(input("[1] Fazer Login\n [2] Quartos disponiveis\n [3] Sair\n Digite sua escolha:"))
        match escolha:
            case 1:
