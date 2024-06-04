def exibir_menu():
    while True:
        print("Menu de opções:")
        print("1 - Cadastrar")
        print("2 - Exibir Mensagem")
        print("3 - Sair")
        opcao=input("Escolha uma opção (1-3): ")
        if opcao.isdigit():
            opcao=int(opcao)
            if 1<=opcao<=3:
                return opcao
        print("Opção inválida. Por favor, escolha uma opção válida.")