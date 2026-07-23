from filme import Filme
from cliente import Cliente
from sessao import Sessao
from ingresso import Ingresso
class Sistema:
    def __init__(self):
        self.filmes = []
        self.clientes = []
        self.sessoes = []
        self.ingressos = []

    def cadastrar_filme(self):
        titulo = input("Digite o título do filme: ")
        genero = input("Digite o gênero do filme: ")
        duracao = int(input("Digite a duração do filme (em minutos): "))
        classificacao_etaria = input("Digite a classificação etária: ")

        novo_filme = Filme(titulo, genero, duracao, classificacao_etaria)
        self.filmes.append(novo_filme)
        print("Filme cadastrado com sucesso!")

    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        tipo_cliente = input("Digite o tipo de cliente (comum ou estudante): ")

        novo_cliente = Cliente (nome, cpf, email, tipo_cliente)
        self.clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso!")

    def cadastrar_sessao(self):
        codigo = input("Digite o código da sessão: ")
        filme = input("Digite o nome do filme: ")
        horario = input("Digite o horário da sessão: ")
        sala = int(input("Digite a sala: "))
        quantidade_assentos = int(input("Digite a quantidade de assentos: "))
        assentos_disponiveis = quantidade_assentos

        nova_sessao = Sessao (filme, horario, sala, quantidade_assentos, assentos_disponiveis)
        self.sessoes.append(nova_sessao)
        print("Sessão cadastrada com sucesso!")

    def cadastrar_ingresso(self):
        cliente = input("Digite o nome do cliente: ")
        codigo_sessao = input("Digite o código da sessão: ")
        valor = float(input("Digite o valor do ingresso: "))
        assento = input("Digite o número do assento: ")

        novo_ingresso = Ingresso (cliente, codigo_sessao, valor, assento)
        self.ingressos.append(novo_ingresso)
        print("Ingresso cadastrado com sucesso!")