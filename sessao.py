class Sessao:
    def __init__(self, codigo, filme, horario, sala, quantidade_assentos, assentos_disponiveis):
        self.codigo =  codigo
        self.filme = filme
        self.horario = horario
        self.sala = sala 
        self.quantidade_assentos = quantidade_assentos
        self.assentos_disponiveis = assentos_disponiveis

    def __str__(self):
                return f"Código: {self.codigo} | Filme: {self.filme} | Horário: {self.horario} | Sala: {self.sala} | Quantidade de assentos: {self.quantidade_assentos} | Assentos disponíveis: {self.assentos_disponiveis}" 
    
class GerenciadorSessoes:
        def __init__(self):
            self.sessoes = []   
    
        # CREAT
        def cadastrar_sessao(self, sessao):
            self.sessoes.append(sessao)
            print(f"\nSessão '{sessao.codigo}' adicionada com sucesso!")
    
        # READ
        def listar_sessoes(self):
            if not self.sessoes:
                print("\nNenhuma sessão cadastrada no momento.")
                return False
            
            print("\n--- LISTA DE SESSÕES ---")
            for i, sessa in enumerate(self.sessoes):  
                print(f"[{i}] {sessa}")               
            return True
    
        # UPDATE
        def atualizar_sessao(self, indice):
            if 0 <= indice < len(self.sessoes):
                print(f"\n--- ATUALIZANDO: {self.sessoes[indice].codigo} ---")
                novo_codigo = input("Novo Código: ")
                novo_filme = input("Novo Filme: ")
                novo_horario = input("Novo Horário: ")
                nova_sala = input("Nova Sala: ")
                nova_quantidade_assentos = int(input("Nova Quantidade de Assentos: "))
                novo_assentos_disponiveis = input("Nova Quantidade de Assentos Disponíveis: ")
    
                self.sessoes[indice] = Sessao(novo_codigo, novo_filme, novo_horario, nova_sala, nova_quantidade_assentos, novo_assentos_disponiveis)
                print("\nSessão atualizada com sucesso!")
            else:
                print("\nPosição (índice) inválida!")
    
        # DELETE
        def excluir_sessao(self, indice):
            if 0 <= indice < len(self.sessoes):
                sessao_removida = self.sessoes.pop(indice)
                print(f"\nSessão '{sessao_removida.codigo}' removida com sucesso!")
            else:
                print("\nPosição (índice) inválida!")
    
    # PROGRAMA PRINCIPAL 
def menu_sessoes():
        gerenciador = GerenciadorSessoes()
    
        while True:
            print("\n" + "="*50)
            print("         SISTEMA CINEMAX - GERENCIAR SESSÕES")
            print("="*50)
            print("1 - Cadastrar Sessão")
            print("2 - Listar Sessões")
            print("3 - Atualizar Sessão")
            print("4 - Excluir Sessão")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ")
    
            if opcao == "1":
                print("\n--- CADASTRO DE SESSÃO ---")
                codigo = input("Código da Sessão: ")
                filme = input("Filme: ")
                horario = input("Horário: ")
                sala = input("Sala: ")
                quantidade_assentos = int(input("Quantidade de Assentos: "))
                assentos_disponiveis = int(input("Assentos Disponíveis: "))
                
                novo = Sessao(codigo, filme, horario, sala, quantidade_assentos, assentos_disponiveis)
                gerenciador.cadastrar_sessao(novo)
    
            elif opcao == "2":
                gerenciador.listar_sessoes()
    
            elif opcao == "3":
                if gerenciador.listar_sessoes():
                    try:
                        posicao = int(input("\nDigite o número [índice] da sessão que deseja atualizar: "))
                        gerenciador.atualizar_sessao(posicao)
                    except ValueError:
                        print("\nPor favor, digite apenas números válidos!")
    
            elif opcao == "4":
                if gerenciador.listar_sessoes():
                    try:
                        posicao = int(input("\nDigite o número [índice] da sessão que deseja excluir: "))
                        gerenciador.excluir_sessao(posicao)
                    except ValueError:
                        print("\nPor favor, digite apenas números válidos!")
    
            elif opcao == "0":
                print("\nRetornando ao menu principal...")
                break
    
            else:
                print("\nOpção inválida. Tente novamente.")
