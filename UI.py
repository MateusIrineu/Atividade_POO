from Cliente import Cliente, ClienteDAO
from Categoria import Categoria, CategoriaDAO
from Produto import Produto, ProdutoDAO

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
    
#CLIENTE
    @staticmethod
    def cliente_inserir():                           
        print("Cadastro de Clientes")
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(c)
    @staticmethod
    def cliente_listar():                            
        print("Listagem de Clientes")
        for c in ClienteDAO.listar():
            print(c)
    @staticmethod
    def cliente_atualizar():                         
        UI.cliente_listar()
        id = int(input("Qual o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(c)
    @staticmethod
    def cliente_excluir():                           
        UI.cliente_listar()
        id = int(input("Qual o id do cliente a ser excluído: "))
        c = Cliente(id, "", "", "")
        ClienteDAO.excluir(c)

#CATEGORIA
    @staticmethod
    def categoria_inserir():                           
        print("Cadastro de Categorias")
        desc = input("Informe a descrição: ")
        c = Categoria(0, desc)
        CategoriaDAO().inserir(c)
    @staticmethod
    def categoria_listar():                            
        print("Listagem de Categorias")
        for c in CategoriaDAO().listar(): print(c)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Qual o id da categoria a ser atualizado: "))
        desc = input("Informe a nova descrição: ")
        c = Categoria(id, desc)
        CategoriaDAO().atualizar(c)

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Qual o id da categoria a ser excluído: "))
        c = Categoria(id, "")
        CategoriaDAO().excluir(c)

# PRODUTO
    @staticmethod
    def produto_inserir():
        print("Cadastro de Produtos")
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        idCategoria = int(input("Insira a categoria do produto: "))
        p = Produto(0, descricao, preco, estoque, idCategoria)
        ProdutoDAO().inserir(p)

    @staticmethod
    def produto_listar():
        print("Listagem de Produtos")
        for p in ProdutoDAO().listar():
            print(p)
    
    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Insira o id do produto a ser atualizado: "))
        descricao = input("Insira a nova descrição: ")
        preco = float(input("Insira o novo preço: "))
        estoque = int(input("Insira a nova quantidade em estoque: "))
        idCategoria = int(input("Insira o id da nova categoria do produto: "))
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO().atualizar(p)
    
    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Insira o id do produto a ser excluído: "))
        p = Produto(id, "", 0.0, 0, 0)
        ProdutoDAO().excluir(p)


UI.main()