class Ingresso:
    def __init__(self, cliente, codigo_sessao, valor, assento):
        self.cliente = cliente
        self.codigo_sessao = codigo_sessao
        self.valor = valor
        self.assento = assento

    def __str__(self):
                return f"Cliente: {self.cliente} | Código da Sessão: {self.codigo_sessao} | Valor: {self.valor} | Assento: {self.assento}"
    
class GerenciadorIngressos:
        def __init__(self):
            self.ingressos = []   
    
        # CREAT
        def cadastrar_ingresso(self, ingresso):
            self.ingressos.append(ingresso)
            print(f"\nIngresso do cliente'{ingresso.cliente}' adicionado com sucesso!")
    
        # READ
        def listar_ingressos(self):
            if not self.ingressos:
                print("\nNenhum ingresso cadastrado no momento.")
                return False
            
            print("\n--- LISTA DE INGRESSOS ---")
            for i, ingress in enumerate(self.ingressos):  
                print(f"[{i}] {ingress}")               
            return True
    
        # UPDATE
        def atualizar_ingresso(self, indice):
            if 0 <= indice < len(self.ingressos):
                print(f"\n--- ATUALIZANDO: {self.ingressos[indice].cliente} ---")
                novo_cliente = input("Novo Cliente: ")
                novo_codigo_sessao = input("Novo Código da Sessão: ")
                novo_valor = input("Novo Valor: ")
                novo_assento = input("Novo Assento: ")
    
                self.ingressos[indice] = Ingresso(novo_cliente, novo_codigo_sessao, novo_valor, novo_assento)
                print("\nIngresso atualizado com sucesso!")
            else:
                print("\nPosição (índice) inválida!")
    
        # DELETE
        def excluir_ingresso(self, indice):
            if 0 <= indice < len(self.ingressos):
                ingresso_removido = self.ingressos.pop(indice)
                print(f"\nIngresso do cliente'{ingresso_removido.cliente}' removido com sucesso!")
            else:
                print("\nPosição (índice) inválida!")
    
    # PROGRAMA PRINCIPAL 
def menu_ingressos():
        gerenciador = GerenciadorIngressos()
    
        while True:
            print("\n" + "="*50)
            print("         SISTEMA CINEMAX - GERENCIAR INGRESSOS")
            print("="*50)
            print("1 - Cadastrar Ingresso")
            print("2 - Listar Ingressos")
            print("3 - Atualizar Ingresso")
            print("4 - Excluir Ingresso")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ")
    
            if opcao == "1":
                print("\n--- CADASTRO DE INGRESSO ---")
                cliente = input("Nome do Cliente: ")
                codigo_sessao = input("Código da Sessão: ")
                valor = int(input("Valor do Ingresso: "))
                assento = input("Assento: ")
                
                novo = Ingresso(cliente, codigo_sessao, valor, assento)
                gerenciador.cadastrar_ingresso(novo)
    
            elif opcao == "2":
                gerenciador.listar_ingressos()
    
            elif opcao == "3":
                if gerenciador.listar_ingressos():
                    try:
                        posicao = int(input("\nDigite o número [índice] do ingresso que deseja atualizar: "))
                        gerenciador.atualizar_ingresso(posicao)
                    except ValueError:
                        print("\nPor favor, digite apenas números válidos!")
    
            elif opcao == "4":
                if gerenciador.listar_ingressos():
                    try:
                        posicao = int(input("\nDigite o número [índice] do ingresso que deseja excluir: "))
                        gerenciador.excluir_ingresso(posicao)
                    except ValueError:
                        print("\nPor favor, digite apenas números válidos!")
    
            elif opcao == "0":
                print("\nRetornando ao menu principal...")
                break
    
            else:
                print("\nOpção inválida. Tente novamente.")
