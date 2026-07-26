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
