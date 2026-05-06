from Admin.Cliente import Cliente, ClienteDAO
from Admin.Categoria import Categoria, CategoriaDAO
from Admin.Produto import Produto, ProdutoDAO

class View:
    #CLIENTE
    @staticmethod
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(c)

    @staticmethod
    def cliente_listar():                            
        return ClienteDAO.listar()
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):                         
        c = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(c)

    @staticmethod
    def cliente_excluir(id):                           
        c = Cliente(id, "", "", "")
        ClienteDAO.excluir(c)

    #CATEGORIA
    @staticmethod
    def categoria_inserir(desc):                           
        c = Categoria(0, desc)
        CategoriaDAO().inserir(c)

    @staticmethod
    def categoria_listar():                            
        return CategoriaDAO().listar()
    
    @staticmethod
    def categoria_atualizar(id, desc):
        c = Categoria(id, desc)
        CategoriaDAO().atualizar(c)

    @staticmethod
    def categoria_excluir(id):
        c = Categoria(id, "")
        CategoriaDAO().excluir(c)

    #PRODUTO
    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        p = Produto(0, descricao, preco, estoque, idCategoria)
        ProdutoDAO().inserir(p)
    
    @staticmethod
    def produto_listar():                            
        return ProdutoDAO().listar()

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO().atualizar(p)

    @staticmethod
    def produto_excluir(id):
        p = Produto(id, "", 0.0, 0, 0)
        ProdutoDAO().excluir(p)