# from Cliente import Cliente, ClienteDAO
# from Categoria import Categoria, CategoriaDAO
# from Produto import Produto, ProdutoDAO
from Admin.View import View as AdminView

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 13:
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
    
    @staticmethod
    def menu():
        print("----- Clientes -----")
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir")
        print("----- Categorias -----")
        print("5-Inserir 6-Listar 7-Atualizar 8-Excluir")
        print("----- Produtos -----")
        print("9-Inserir 10-Listar 11-Atualizar 12-Excluir")
        print("13-Fim")
        return int(input("Informe uma opção: "))
    
#CLIENTE POR ADMIN
    
    def cliente_inserir():                           
        print("Cadastro de Clientes")
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        # c = View(0, nome, email, fone)
        AdminView.cliente_inserir(nome, email, fone)

    def cliente_listar():                            
        print("Listagem de Clientes")
        for c in View.cliente_listar():
            print(c)

    def cliente_atualizar():                         
        UI.cliente_listar()
        id = int(input("Qual o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        # c = Cliente(id, nome, email, fone)
        AdminView.cliente_atualizar(id, nome, email, fone)

    def cliente_excluir():                           
        UI.cliente_listar()
        id = int(input("Qual o id do cliente a ser excluído: "))
        # c = Cliente(id, "", "", "")
        AdminView.cliente_excluir(id)

#CATEGORIA POR ADMIN
    def categoria_inserir():                           
        print("Cadastro de Categorias")
        desc = input("Informe a descrição: ")
        # c = Categoria(0, desc)
        AdminView.categoria_inserir(desc)

    def categoria_listar():                            
        print("Listagem de Categorias")
        for c in AdminView.categoria_listar(): 
            print(c)

    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Qual o id da categoria a ser atualizado: "))
        desc = input("Informe a nova descrição: ")
        # c = Categoria(id, desc)
        AdminView.categoria_atualizar(id, desc)

    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Qual o id da categoria a ser excluído: "))
        # c = Categoria(id, "")
        AdminView.categoria_excluir(id)

# PRODUTO POR ADMIN

    def produto_inserir():
        print("Cadastro de Produtos")
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        idCategoria = int(input("Insira a categoria do produto: "))
        # p = Produto(0, descricao, preco, estoque, idCategoria)
        AdminView.produto_inserir(descricao, preco, estoque, idCategoria)

    def produto_listar():
        print("Listagem de Produtos")
        for p in AdminView.produto_listar():
            print(p)
    
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Insira o id do produto a ser atualizado: "))
        descricao = input("Insira a nova descrição: ")
        preco = float(input("Insira o novo preço: "))
        estoque = int(input("Insira a nova quantidade em estoque: "))
        idCategoria = int(input("Insira o id da nova categoria do produto: "))
        # p = Produto(id, descricao, preco, estoque, idCategoria)
        AdminView.produto_atualizar(id, descricao, preco, estoque, idCategoria)
    
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Insira o id do produto a ser excluído: "))
        # p = Produto(id, "", 0.0, 0, 0)
        AdminView.produto_excluir(id)


UI.main()