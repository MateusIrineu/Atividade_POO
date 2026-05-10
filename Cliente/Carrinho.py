import json

class Carrinho:
    def __init__ (self, id: int, idProduto: int, descricao: str, quantidade: int):
        self.id = id
        self.idProduto = idProduto
        self.descricao = descricao
        self.quantidade = quantidade
    def __str__(self) -> str:
        return f"Carrinho #{self.id} - Produto #{self.idProduto} - {self.descricao} - Quantidade: {self.quantidade}"
    
class CarrinhoDAO:
    objetos = []
    produtos_comprados = []

    @staticmethod
    def inserir_produto_carrinho(obj):
        CarrinhoDAO.abrir()

        if len(CarrinhoDAO.objetos) == 0:
            obj.id = 1
        else:
            obj.id = CarrinhoDAO.objetos[0].id 
    
        CarrinhoDAO.objetos.append(obj)
        CarrinhoDAO.salvar()

    @staticmethod
    def comprar_carrinho():
        CarrinhoDAO.abrir()
        if len(CarrinhoDAO.objetos) == 0:
            return False
        
        if len(CarrinhoDAO.produtos_comprados) == 0:
            id = 1
        else:
            id = (max(CarrinhoDAO.produtos_comprados, key = lambda x : x.id)).id + 1

        for obj in CarrinhoDAO.objetos:
            obj.id = id
            CarrinhoDAO.produtos_comprados.append(obj)

        CarrinhoDAO.objetos = []
        CarrinhoDAO.salvar()
        return True
    
    @staticmethod
    def limpar_carrinho():
        CarrinhoDAO.abrir()
        CarrinhoDAO.objetos = []
        CarrinhoDAO.salvar()

    @staticmethod
    def visualizar_carrinho():
        CarrinhoDAO.abrir()
        CarrinhoDAO.objetos.sort(key = lambda x : x.idProduto)
        return CarrinhoDAO.objetos
    
    @staticmethod
    def listar_compras():
        CarrinhoDAO.abrir()
        CarrinhoDAO.produtos_comprados.sort(key = lambda x : x.id)
        return CarrinhoDAO.produtos_comprados

    @staticmethod
    def salvar():
        with open("Cliente/carrinhos.json", mode="w") as arquivo:
            json.dump({"objetos": CarrinhoDAO.objetos, "produtos_comprados": CarrinhoDAO.produtos_comprados}, arquivo, default = vars)  
                           
    @staticmethod
    def abrir():
        CarrinhoDAO.objetos = []
        CarrinhoDAO.produtos_comprados = []
        try:
            with open("Cliente/carrinhos.json", mode="r") as arquivo:
                dados = json.load(arquivo)
                for obj in dados.get("objetos", []):
                    c = Carrinho(obj["id"], obj["idProduto"], obj["descricao"], obj["quantidade"])
                    CarrinhoDAO.objetos.append(c)
                for obj in dados.get("produtos_comprados", []):
                    c = Carrinho(obj["id"], obj["idProduto"], obj["descricao"], obj["quantidade"])
                    CarrinhoDAO.produtos_comprados.append(c)
        except FileNotFoundError:
            pass