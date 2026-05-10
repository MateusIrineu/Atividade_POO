from .Carrinho import Carrinho, CarrinhoDAO
from Admin.Produto import Produto, ProdutoDAO

class View:
    # CARRINHO
    @staticmethod
    def listar_produtos():
        return ProdutoDAO().listar()
    
    @staticmethod
    def inserir_produto_carrinho(idProduto, quantidade):
        produto = ProdutoDAO().listar_id(idProduto)

        if produto is None:
            return False
        
        carrinho_item = Carrinho(id = 0, idProduto = idProduto, descricao = produto.descricao, quantidade = quantidade)

        CarrinhoDAO().inserir_produto_carrinho(carrinho_item)
        return True
    
    @staticmethod
    def visualizar_carrinho():
        return CarrinhoDAO().visualizar_carrinho()
    
    @staticmethod
    def comprar_carrinho():
        return CarrinhoDAO().comprar_carrinho()
    
    @staticmethod
    def listar_compras():
        return CarrinhoDAO().listar_compras()
    
    @staticmethod
    def limpar_carrinho():
        return CarrinhoDAO().limpar_carrinho()