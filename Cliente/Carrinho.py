import json
from datetime import datetime
from Admin.Venda import Venda, VendaDAO
from Admin.VendaItem import VendaItem, VendaItemDAO
from Admin.Produto import ProdutoDAO

class CarrinhoItem:
    def __init__(self, idProduto: int, descricao: str, quantidade: int, preco: float):
        self.idProduto = idProduto
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
    
    def __str__(self) -> str:
        return f"Produto #{self.idProduto} - {self.descricao} - Quantidade: {self.quantidade} - Preço: {self.preco}"

class Carrinho:
    def __init__(self, id: int, idCliente: int):
        self.id = id
        self.idCliente = idCliente
        self.itens = []
    
    def __str__(self) -> str:
        return f"Carrinho #{self.id} - Cliente #{self.idCliente} - {len(self.itens)} itens"
    
class CarrinhoDAO:
    carrinhos = {}
    produtos_comprados = []

    @staticmethod
    def obter_ou_criar_carrinho(idCliente):
        """Obtém o carrinho do cliente ou cria um novo se não existir"""
        if idCliente not in CarrinhoDAO.carrinhos:
            # Cria novo carrinho para o cliente
            novo_id = max([int(k) for k in CarrinhoDAO.carrinhos.keys()], default=0) + 1
            CarrinhoDAO.carrinhos[str(idCliente)] = Carrinho(novo_id, idCliente)
        return CarrinhoDAO.carrinhos[str(idCliente)]

    @staticmethod
    def inserir_produto_carrinho(idCliente, idProduto, descricao, quantidade, preco):
        CarrinhoDAO.abrir()
        carrinho = CarrinhoDAO.obter_ou_criar_carrinho(idCliente)
        
        item = CarrinhoItem(idProduto, descricao, quantidade, preco)
        carrinho.itens.append(item)
        CarrinhoDAO.salvar()

    @staticmethod
    def comprar_carrinho(idCliente):
        CarrinhoDAO.abrir()
        
        if str(idCliente) not in CarrinhoDAO.carrinhos:
            return False
        
        carrinho = CarrinhoDAO.carrinhos[str(idCliente)]
        if len(carrinho.itens) == 0:
            return False
        
        # Calcula total
        total = 0.0
        for item in carrinho.itens:
            total += item.preco * item.quantidade
        
        # Cria Venda
        venda = Venda(0, datetime.now(), False, total, idCliente)
        VendaDAO.inserir(venda)
        venda_id = venda.id
        
        # Cria VendaItem para cada item do carrinho
        for item in carrinho.itens:
            venda_item = VendaItem(0, item.quantidade, item.preco, venda_id, item.idProduto)
            VendaItemDAO.inserir(venda_item)
        
        # Limpa carrinho
        carrinho.itens = []
        CarrinhoDAO.salvar()
        return True
    
    @staticmethod
    def limpar_carrinho(idCliente):
        CarrinhoDAO.abrir()
        if str(idCliente) in CarrinhoDAO.carrinhos:
            CarrinhoDAO.carrinhos[str(idCliente)].itens = []
            CarrinhoDAO.salvar()

    @staticmethod
    def visualizar_carrinho(idCliente):
        CarrinhoDAO.abrir()
        if str(idCliente) not in CarrinhoDAO.carrinhos:
            return []
        return CarrinhoDAO.carrinhos[str(idCliente)].itens
    
    @staticmethod
    def listar_compras(idCliente):
        CarrinhoDAO.abrir()
        compras_cliente = [obj for obj in CarrinhoDAO.produtos_comprados if obj.get("idCliente") == idCliente]
        return compras_cliente

    @staticmethod
    def salvar():
        carrinhos_dict = {}
        for chave, carrinho in CarrinhoDAO.carrinhos.items():
            carrinhos_dict[chave] = {
                "id": carrinho.id,
                "idCliente": carrinho.idCliente,
                "itens": [vars(item) for item in carrinho.itens]
            }
        
        with open("Cliente/carrinhos.json", mode="w") as arquivo:
            json.dump({
                "carrinhos": carrinhos_dict,
                "produtos_comprados": CarrinhoDAO.produtos_comprados
            }, arquivo, indent=4)
                           
    @staticmethod
    def abrir():
        CarrinhoDAO.carrinhos = {}
        CarrinhoDAO.produtos_comprados = []
        try:
            with open("Cliente/carrinhos.json", mode="r") as arquivo:
                dados = json.load(arquivo)
                
                # Carrega carrinhos
                for chave, carrinho_data in dados.get("carrinhos", {}).items():
                    carrinho = Carrinho(carrinho_data["id"], carrinho_data["idCliente"])
                    for item_data in carrinho_data.get("itens", []):
                        item = CarrinhoItem(
                            item_data["idProduto"],
                            item_data["descricao"],
                            item_data["quantidade"],
                            item_data["preco"]
                        )
                        carrinho.itens.append(item)
                    CarrinhoDAO.carrinhos[chave] = carrinho
                
                # Carrega histórico de compras
                CarrinhoDAO.produtos_comprados = dados.get("produtos_comprados", [])
        except FileNotFoundError:
            pass