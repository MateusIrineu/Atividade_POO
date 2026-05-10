# from Cliente import Cliente, ClienteDAO
# from Categoria import Categoria, CategoriaDAO
# from Produto import Produto, ProdutoDAO
from Admin.View import View as AdminView
from Visitante.View import View as LoginView
from Cliente.View import View as ClienteView

class UI:
    #CRIAÇÃO DE CONTA OU LOGIN
    @staticmethod
    def home():
        print("Digite 1 para criar conta.")
        print("Digite 2 para criar logar no sistema.")
        print("Digite 0 para fechar o sistema.")
        resposta = int(input("Resposta: "))
        if resposta == 1:
            UI.criar_usuario()
        elif resposta == 2:
            UI.validacao()
        else:
            print("Fechando o sistema...")
    
    #CRIANDO USUARIO
    @staticmethod
    def criar_usuario():                           
        print("Cadastro de Clientes")
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        fone = input("Informe o fone: ")
        # c = View(0, nome, email, fone)
        AdminView.cliente_inserir(nome, email, senha, fone)
        UI.home()

    #VALIDAÇÃO DE USUÁRIO
    @staticmethod
    def validacao():
        print("Forneça seu email e senha para logar no sistema: ")
        email = input("Email: ")
        senha = input("Senha: ")

        if LoginView.login(email, senha): #retorna o bool da função para adm
            if (email == "admin@gmail.com") and (senha == "1234"):
                print("ADMIN logado.")
                UI.main()
            else: #retorna o bool da função para cliente
                print("Login realizado com sucesso!")
                UI.cliente_main()
        else:
            print("Email e/ou senha incorretos!")
            UI.validacao()

    #TELA DE ACESSO DO ADMIN
    @staticmethod
    def main():
        op = 0
        while True:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()
            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()
            if op == 13: UI.validacao()

    #TELA DE ACESSO DO CLIENTE
    @staticmethod
    def cliente_main():
        op = 0
        while True:
            op = UI.cliente_menu()
            if op == 1: UI.inserir_produto()
            if op == 2: UI.listar_produtos()
            if op == 3: UI.listar_compras()
            if op == 4: UI.visualizar_carrinho()
            if op == 5: UI.comprar_carrinho()
            if op == 6: UI.limpar_carrinho()
            if op == 7: UI.validacao()


    #MENU ADMIN
    @staticmethod
    def menu():
        print("----- Clientes -----")
        print("1 - Inserir 2 - Listar 3 - Atualizar 4 - Excluir")
        print("----------------------------------------")
        print("----- Categorias -----")
        print("5 - Inserir 6 - Listar 7 - Atualizar 8 - Excluir")
        print("----------------------------------------")
        print("----- Produtos -----")
        print("9 - Inserir 10 - Listar 11 - Atualizar 12 - Excluir")
        print("----------------------------------------")
        print("13 - Sair do sistema")
        #UI.validacao()
        return int(input("Informe uma opção: "))
    
    #MENU CLIENTE
    @staticmethod
    def cliente_menu():
        print("1 - Inserir produto")
        print("2 - Listar produtos")
        print("3 - Listar Compras")
        print("4 - Visualizar Carrinho")
        print("5 - Comprar Carrinho")
        print("6 - Limpar Carrinho")
        print("7 - Sair do Sistema")
        return int(input("Informe uma opção: "))
    
#CLIENTE POR ADMIN
    @staticmethod
    def cliente_inserir():                           
        print("Cadastro de Clientes")
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        fone = input("Informe o fone: ")
        # c = View(0, nome, email, fone)
        AdminView.cliente_inserir(nome, email, senha, fone)

    @staticmethod
    def cliente_listar():                            
        print("Listagem de Clientes")
        for c in AdminView.cliente_listar():
            print(c)

    @staticmethod
    def cliente_atualizar():                         
        UI.cliente_listar()
        id = int(input("Qual o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        senha = input("Informe a nova senha: ")
        fone = input("Informe o novo fone: ")
        # c = Cliente(id, nome, email, fone)
        AdminView.cliente_atualizar(id, nome, email, senha, fone)

    @staticmethod
    def cliente_excluir():                           
        UI.cliente_listar()
        id = int(input("Qual o id do cliente a ser excluído: "))
        # c = Cliente(id, "", "", "")
        AdminView.cliente_excluir(id)

#CATEGORIA POR ADMIN
    @staticmethod
    def categoria_inserir():                           
        print("Cadastro de Categorias")
        desc = input("Informe a descrição: ")
        # c = Categoria(0, desc)
        AdminView.categoria_inserir(desc)

    @staticmethod
    def categoria_listar():                            
        print("Listagem de Categorias")
        for c in AdminView.categoria_listar(): 
            print(c)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Qual o id da categoria a ser atualizado: "))
        desc = input("Informe a nova descrição: ")
        # c = Categoria(id, desc)
        AdminView.categoria_atualizar(id, desc)

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Qual o id da categoria a ser excluído: "))
        # c = Categoria(id, "")
        AdminView.categoria_excluir(id)

# PRODUTO POR ADMIN
    @staticmethod
    def produto_inserir():
        print("Cadastro de Produtos")
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        idCategoria = int(input("Insira a categoria do produto: "))
        # p = Produto(0, descricao, preco, estoque, idCategoria)
        AdminView.produto_inserir(descricao, preco, estoque, idCategoria)

    @staticmethod
    def produto_listar():
        print("Listagem de Produtos")
        for p in AdminView.produto_listar():
            print(p)

    @staticmethod   
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Insira o id do produto a ser atualizado: "))
        descricao = input("Insira a nova descrição: ")
        preco = float(input("Insira o novo preço: "))
        estoque = int(input("Insira a nova quantidade em estoque: "))
        idCategoria = int(input("Insira o id da nova categoria do produto: "))
        # p = Produto(id, descricao, preco, estoque, idCategoria)
        AdminView.produto_atualizar(id, descricao, preco, estoque, idCategoria)

    @staticmethod  
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Insira o id do produto a ser excluído: "))
        # p = Produto(id, "", 0.0, 0, 0)
        AdminView.produto_excluir(id)

# CLIENTE (CARRINHO E COMPRAS)
    @staticmethod
    def listar_produtos():
        print("Listagem de Produtos Disponíveis")
        for p in ClienteView.listar_produtos():
            print(p)

    @staticmethod
    def inserir_produto():
        UI.listar_produtos()
        idProduto = int(input("Insira o id do produto a adicionar: "))
        quantidade = int(input("Informe a quantidade: "))
        if ClienteView.inserir_produto_carrinho(idProduto, quantidade):
            print("Produto adicionado ao carrinho!")
        else:
            print("Produto não encontrado!")

    @staticmethod
    def visualizar_carrinho():
        print("Itens do Carrinho")
        itens = ClienteView.visualizar_carrinho()
        if len(itens) == 0:
            print("Carrinho vazio!")
        else:
            for item in itens:
                print(item)

    @staticmethod
    def comprar_carrinho():
        if ClienteView.comprar_carrinho():
            print("Compra realizada com sucesso!")
        else:
            print("Carrinho vazio!")

    @staticmethod
    def listar_compras():
        print("Histórico de Compras")
        compras = ClienteView.listar_compras()
        if len(compras) == 0:
            print("Nenhuma compra realizada!")
        else:
            for compra in compras:
                print(compra)

#FUNÇÃO ADICIONAL
    @staticmethod
    def limpar_carrinho():
        ClienteView.limpar_carrinho()
        print("Carrinho limpo!")


UI.home()