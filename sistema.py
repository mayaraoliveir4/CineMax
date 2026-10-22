from filme import menu_filmes
from cliente import menu_clientes
from sessao import menu_sessoes
from ingresso import menu_ingressos

while True:
    print("\n" + "=" * 50)
    print("        SISTEMA CINEMAX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Gerenciar Filmes")
    print("2 - Gerenciar Clientes")
    print("3 - Gerenciar Sessões")
    print("4 - Gerenciar Ingressos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu_filmes()

    elif opcao == "2":
        menu_clientes()

    elif opcao == "3":
        menu_sessoes()

    elif opcao == "4":
        menu_ingressos()

    elif opcao == "0":
        print("\nEncerrando o sistema CineMax. Até logo!")
        break

    else:
        print("\nOpção inválida!")