from pathlib import Path
import csv

# CONFIGURAÇÃO DO ARQUIVO

DIRETORIO_DADOS = Path("dados")

DIRETORIO_DADOS.mkdir(exist_ok=True)

ARQUIVO_CLIENTES = DIRETORIO_DADOS / "clientes.csv"

# CLASSE CLIENTE – representa um cliente individual

class Cliente:
    def __init__(self, nome, cpf, email, tipo_cliente):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.tipo_cliente = tipo_cliente

    def __str__(self):
            return f"Nome: {self.nome} | CPF: {self.cpf} | E-mail: {self.email} | Tipo: {self.tipo_cliente}"

    def para_csv(self):
        return [
            self.nome,
            self.cpf,
            self.email,
            self.tipo_cliente
        ]

# SALVAR

def salvar_clientes(clientes):

    with open(ARQUIVO_CLIENTES, 
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(
            ["nome", "cpf", "email", "tipo_cliente"]
        )

        for cliente in clientes:
            escritor.writerow(
                cliente.para_csv()
            )

    print("\nCliente cadastrado(a) com sucesso!")

# CARREGAR

def carregar_clientes():

    clientes = []

    # Verifica se o arquivo existe
    if not ARQUIVO_CLIENTES.exists():
        return clientes

    with open(
        ARQUIVO_CLIENTES,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.reader(arquivo)

        # Ignora o cabeçalho
        next(leitor, None)

        for linha in leitor:

            nome = linha[0]
            cpf = linha[1]
            email = linha[2]
            tipo_cliente = linha[3]

            cliente = Cliente(
                nome,
                cpf,
                email,
                tipo_cliente
            )

            clientes.append(cliente)

    return clientes

 # CLASSE GERENCIADORCLIENTES – gerencia a lista de clientes (CRUD)

class GerenciadorClientes:
    def __init__(self):
        self.clientes = carregar_clientes() 

    # CREAT
    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"\nCliente '{cliente.nome}' adicionado com sucesso!")

    # READ
    def listar_clientes(self):
        if not self.clientes:
            print("\nNenhum cliente cadastrado no momento.")
            return False
        
        print("\n--- LISTA DE CLIENTES ---")
        for i, client in enumerate(self.clientes):  
            print(f"[{i}] {client}")               
        return True

    # UPDATE
    def atualizar_cliente(self, indice):
        if 0 <= indice < len(self.clientes):
            print(f"\n--- ATUALIZANDO: {self.clientes[indice].nome} ---")
            novo_nome = input("Novo Nome: ")
            novo_cpf = input("Novo CPF: ")
            novo_email = input("Novo E-Mail: ")
            novo_tipo_cliente = input("Novo Tipo de Cliente: ")

            self.clientes[indice] = Cliente(novo_nome, novo_cpf, novo_email, novo_tipo_cliente)
            print("\nCliente atualizado com sucesso!")
        else:
            print("\nPosição (índice) inválida!")

    # DELETE
    def excluir_cliente(self, indice):
        if 0 <= indice < len(self.clientes):
            cliente_removido = self.clientes.pop(indice)
            print(f"\nCliente '{cliente_removido.nome}' removido com sucesso!")
        else:
            print("\nPosição (índice) inválida!")

# PROGRAMA PRINCIPAL 
def menu_clientes():
    gerenciador = GerenciadorClientes()

    while True:
        print("\n" + "="*50)
        print("         SISTEMA CINEMAX - GERENCIAR CLIENTES")
        print("="*50)
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- CADASTRO DE CLIENTE ---")
            nome = input("Nome do Cliente: ")
            cpf = input("CPF: ")
            email = input("E-mail: ")
            tipo_cliente = input("Tipo de Cliente: ")
            
            novo = Cliente(nome, cpf, email, tipo_cliente)
            gerenciador.cadastrar_cliente(novo)

            salvar_clientes(gerenciador.clientes)

        elif opcao == "2":
            gerenciador.listar_clientes()

        elif opcao == "3":
            if gerenciador.listar_clientes():
                try:
                    posicao = int(input("\nDigite o número [índice] do cliente que deseja atualizar: "))
                    gerenciador.atualizar_cliente(posicao)
                    salvar_clientes(gerenciador.clientes)
                except ValueError:
                    print("\nPor favor, digite apenas números válidos!")

        elif opcao == "4":
            if gerenciador.listar_clientes():
                try:
                    posicao = int(input("\nDigite o número [índice] do cliente que deseja excluir: "))
                    gerenciador.excluir_cliente(posicao)
                    salvar_clientes(gerenciador.clientes)
                except ValueError:
                    print("\nPor favor, digite apenas números válidos!") 

        elif opcao == "0":
            print("\nRetornando ao menu principal...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")