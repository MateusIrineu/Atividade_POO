from .Carrinho import Carrinho, CarrinhoDAO
from Admin.Produto import Produto, ProdutoDAO
from Admin.Promocao import PromocaoDAO

class View:
    # CARRINHO
    @staticmethod
    def listar_produtos():
        produtos = ProdutoDAO().listar()
        resultado = []
        for p in produtos:
            desconto = PromocaoDAO.obter_desconto_categoria(p.idCategoria)
            if desconto > 0:
                preco_com_desconto = round(p.preco * (1 - desconto / 100), 2)
                resultado.append({
                    "Id": p.id,
                    "Nome": p.descricao,
                    "Preço Original": f"R$ {p.preco:.2f}",
                    "Preço com Desconto": f"R$ {preco_com_desconto:.2f} ({desconto:.0f}% OFF)",
                    "Estoque": p.estoque,
                    "Imagem": f"data:image/png;base64,{p.imagem}" if p.imagem else None
                })
            else:
                resultado.append({
                    "Id": p.id,
                    "Nome": p.descricao,
                    "Preço Original": f"R$ {p.preco:.2f}",
                    "Preço com Desconto": "-",
                    "Estoque": p.estoque,
                    "Imagem": f"data:image/png;base64,{p.imagem}" if p.imagem else None
                })
        return resultado

    @staticmethod
    def inserir_produto_carrinho(idCliente, idProduto, quantidade):
        produto = ProdutoDAO().listar_id(idProduto)

        if produto is None:
            return False

        desconto = PromocaoDAO.obter_desconto_categoria(produto.idCategoria)
        preco_final = round(produto.preco * (1 - desconto / 100), 2) if desconto > 0 else produto.preco

        CarrinhoDAO.inserir_produto_carrinho(idCliente, idProduto, produto.descricao, quantidade, preco_final)
        return True
    
    @staticmethod
    def visualizar_carrinho(idCliente):
        return CarrinhoDAO.visualizar_carrinho(idCliente)
    
    @staticmethod
    def comprar_carrinho(idCliente):
        return CarrinhoDAO.comprar_carrinho(idCliente)
    
    @staticmethod
    def listar_compras(idCliente):
        return CarrinhoDAO.listar_compras(idCliente)
    
    @staticmethod
    def limpar_carrinho(idCliente):
        return CarrinhoDAO.limpar_carrinho(idCliente)

    @staticmethod
    def total_carrinho_com_desconto(idCliente):
        return CarrinhoDAO.total_com_desconto(idCliente)
