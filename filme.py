<<<<<<< HEAD
from pathlib import Path
import csv

# CONFIGURAÇÃO DO ARQUIVO

DIRETORIO_DADOS = Path("dados")

DIRETORIO_DADOS.mkdir(exist_ok=True)

ARQUIVO_FILMES = DIRETORIO_DADOS / "filmes.csv"

# CLASSE FILME – representa um filme individual

class Filme:
    def __init__(self, titulo, genero, duracao, classificacao_etaria): 
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.classificacao_etaria = classificacao_etaria

    def __str__(self):
        return f"Título: {self.titulo} | Gênero: {self.genero} | Duração: {self.duracao} | Classificação: {self.classificacao_etaria}"

    def para_csv(self):
        return [
            self.titulo,
            self.genero,
            self.duracao,
            self.classificacao_etaria
        ]

# SALVAR

def salvar_filmes(filmes):

    with open(ARQUIVO_FILMES, 
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(
            ["titulo", "genero", "duracao", "classificacao_etaria"]
        )

        for filme in filmes:
            escritor.writerow(
                filme.para_csv()
            )

    print("\nFilme cadastrado com sucesso!")

# CARREGAR

def carregar_filmes():

    filmes = []

    # Verifica se o arquivo existe
    if not ARQUIVO_FILMES.exists():
        return filmes

    with open(
        ARQUIVO_FILMES,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.reader(arquivo)

        # Ignora o cabeçalho
        next(leitor, None)

        for linha in leitor:

            titulo = linha[0]
            genero = linha[1]
            duracao = linha[2]
            classificacao_etaria = linha[3]

            filme = Filme(
                titulo,
                genero,
                duracao,
                classificacao_etaria
            )

            filmes.append(filme)

    return filmes

# CLASSE GERENCIADORFILMES – gerencia a lista de filmes (CRUD)

class GerenciadorFilmes:
    # Carrega os filmes que já estão salvos
    def __init__(self):
        self.filmes = carregar_filmes()

    # C - CREATE: Adicionar filme no FINAL da lista
    def cadastrar_filme(self, filme):
        self.filmes.append(filme)
        print(f"\nFilme '{filme.titulo}' adicionado com sucesso!")

    # R - READ: Listar todos os filmes com seus índices (posições)
    def listar_filmes(self):
        if not self.filmes:
            print("\nNenhum filme cadastrado no momento.")
            return False
        
        print("\n--- LISTA DE FILMES ---")
        for i, film in enumerate(self.filmes):   # i = índice, film = filme
            print(f"[{i}] {film}")               # usa o __str__ do Filme
        return True

    # U - UPDATE: Atualizar dados de um filme existente
    def atualizar_filme(self, indice):
        if 0 <= indice < len(self.filmes):
            print(f"\n--- ATUALIZANDO: {self.filmes[indice].titulo} ---")
            novo_titulo = input("Novo Título: ")
            novo_genero = input("Novo Gênero: ")
            nova_duracao = input("Nova Duração: ")
            nova_classificacao = input("Nova Classificação: ")

            self.filmes[indice] = Filme(novo_titulo, novo_genero, nova_duracao, nova_classificacao)
            print("\nFilme atualizado com sucesso!")
        else:
            print("\nPosição (índice) inválida!")

    # D - DELETE: Excluir um filme da lista
    def excluir_filme(self, indice):
        if 0 <= indice < len(self.filmes):
            filme_removido = self.filmes.pop(indice)
            print(f"\nFilme '{filme_removido.titulo}' removido com sucesso!")
        else:
            print("\nPosição (índice) inválida!")


# PROGRAMA PRINCIPAL – interface com o usuário (menu)

def menu_filmes():
    gerenciador = GerenciadorFilmes()

    while True:
        print("\n" + "="*50)
        print("         SISTEMA CINEMAX - GERENCIAR FILMES")
        print("="*50)
        print("1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("3 - Atualizar Filme")
        print("4 - Excluir Filme")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- CADASTRO DE FILME ---")
            titulo = input("Título do Filme: ")
            genero = input("Gênero: ")
            duracao = input("Duração: ")
            classificacao = input("Classificação Etária: ")
            
            novo = Filme(titulo, genero, duracao, classificacao)
            gerenciador.cadastrar_filme(novo)

            salvar_filmes(gerenciador.filmes)
            
        elif opcao == "2":
            gerenciador.listar_filmes()

        elif opcao == "3":
            if gerenciador.listar_filmes():
                try:
                    posicao = int(input("\nDigite o número [índice] do filme que deseja atualizar: "))
                    gerenciador.atualizar_filme(posicao)
                    salvar_filmes(gerenciador.filmes)
                except ValueError:
                    print("\nPor favor, digite apenas números válidos!")

        elif opcao == "4":
            if gerenciador.listar_filmes():
                try:
                    posicao = int(input("\nDigite o número [índice] do filme que deseja excluir: "))
                    gerenciador.excluir_filme(posicao)
                    salvar_filmes(gerenciador.filmes)
                except ValueError:
                    print("\nPor favor, digite apenas números válidos!")

        elif opcao == "0":
            print("\nRetornando ao menu principal...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")
=======
# ------------------------------------------------------------
# CLASSE FILME – representa um filme individual
# ------------------------------------------------------------
class Filme:
    # Método construtor: é chamado automaticamente ao criar um novo filme
    def __init__(self, titulo, genero, duracao, classificacao_etaria): 
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.classificacao_etaria = classificacao_etaria

    # Método especial que define como o filme será exibido quando usado print()
    def __str__(self):
        return f"Título: {self.titulo} | Gênero: {self.genero} | Duração: {self.duracao} | Classificação: {self.classificacao_etaria}"


# ------------------------------------------------------------
# CLASSE GERENCIADORFILMES – gerencia a lista de filmes (CRUD)
# ------------------------------------------------------------
class GerenciadorFilmes:
    # Construtor: cria uma lista vazia para armazenar os filmes
    def __init__(self):
        self.filmes = []   # lista vazia que guardará objetos do tipo Filme

    # C - CREATE: Adicionar filme no FINAL da lista
    def cadastrar_filme(self, filme):
        """Recebe um objeto Filme e insere na lista."""
        self.filmes.append(filme)
        print(f"\nFilme '{filme.titulo}' adicionado com sucesso!")

    # R - READ: Listar todos os filmes com seus índices (posições)
    def listar_filmes(self):
        """Exibe todos os filmes, numerados a partir de 0."""
        if not self.filmes:
            print("\nNenhum filme cadastrado no momento.")
            return False
        
        print("\n--- LISTA DE FILMES ---")
        for i, film in enumerate(self.filmes):   # i = índice, film = filme
            print(f"[{i}] {film}")               # usa o __str__ do Filme
        return True

    # U - UPDATE: Atualizar dados de um filme existente
    def atualizar_filme(self, indice):
        """Substitui os dados do filme na posição indicada."""
        if 0 <= indice < len(self.filmes):
            print(f"\n--- ATUALIZANDO: {self.filmes[indice].titulo} ---")
            novo_titulo = input("Novo Título: ")
            novo_genero = input("Novo Gênero: ")
            nova_duracao = input("Nova Duração: ")
            nova_classificacao = input("Nova Classificação: ")

            # Criamos o filme atualizado e substituímos no mesmo índice da lista
            self.filmes[indice] = Filme(novo_titulo, novo_genero, nova_duracao, nova_classificacao)
            print("\nFilme atualizado com sucesso!")
        else:
            print("\nPosição (índice) inválida!")

    # D - DELETE: Excluir um filme da lista
    def excluir_filme(self, indice):
        """Remove o filme da lista com base na sua posição."""
        if 0 <= indice < len(self.filmes):
            filme_removido = self.filmes.pop(indice)
            print(f"\nFilme '{filme_removido.titulo}' removido com sucesso!")
        else:
            print("\nPosição (índice) inválida!")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL – interface com o usuário (menu)
# ------------------------------------------------------------
def menu_filmes():
    gerenciador = GerenciadorFilmes()

    while True:
        print("\n" + "="*50)
        print("         SISTEMA CINEMAX - GERENCIAR FILMES")
        print("="*50)
        print("1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("3 - Atualizar Filme")
        print("4 - Excluir Filme")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- CADASTRO DE FILME ---")
            titulo = input("Título do Filme: ")
            genero = input("Gênero: ")
            duracao = input("Duração: ")
            classificacao = input("Classificação Etária: ")
            
            novo = Filme(titulo, genero, duracao, classificacao)
            gerenciador.cadastrar_filme(novo)

        elif opcao == "2":
            gerenciador.listar_filmes()

        elif opcao == "3":
            # Primeiro listamos os filmes para o usuário ver quais números existem
            if gerenciador.listar_filmes():
                try:
                    posicao = int(input("\nDigite o número [índice] do filme que deseja atualizar: "))
                    gerenciador.atualizar_filme(posicao)
                except ValueError:
                    print("\nPor favor, digite apenas números válidos!")

        elif opcao == "4":
            if gerenciador.listar_filmes():
                try:
                    posicao = int(input("\nDigite o número [índice] do filme que deseja excluir: "))
                    gerenciador.excluir_filme(posicao)
                except ValueError:
                    print("\nPor favor, digite apenas números válidos!")

        elif opcao == "0":
            print("\nRetornando ao menu principal...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")
>>>>>>> b9c74da9fb569b8e93644e2b6713a29db27e1632
