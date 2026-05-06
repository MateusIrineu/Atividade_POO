import json
from datetime import datetime

class Venda:
    def __init__(self, id: int, data: datetime, carrinho: bool, total: float, idCliente: int):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.idCliente = idCliente
    
    def __str__(self) -> str:
        return f"{self.id} - {self.data} - {self.carrinho} - {self.total} - {self.idCliente}"
    
class VendaDAO:
    objetos: list[Venda] = []
    @staticmethod
    def inserir(obj: Venda) -> None:
        VendaDAO.abrir()
        if len(VendaDAO.objetos) == 0:
            id = 1

        else:
            id = (max(VendaDAO.objetos, key = lambda x : x.id)).id + 1

        obj.id = id
        VendaDAO.objetos.append(obj)
        VendaDAO.salvar()

    @staticmethod
    def listar() -> list[Venda]:
        VendaDAO.abrir()
        VendaDAO.objetos.sort(key = lambda x : x.id)
        return VendaDAO.objetos
    
    @staticmethod
    def listar_id(id: int) -> Venda | None:
        VendaDAO.abrir()
        for obj in VendaDAO.objetos:
            if obj.id == id:
                return obj
        return None
    
    @staticmethod
    def atualizar(obj: Venda) -> None:
        x = VendaDAO.listar_id(obj.id)
        if x != None:
            VendaDAO.objetos.remove(x)
            VendaDAO.objetos.append(obj)
            VendaDAO.salvar()

    @staticmethod
    def excluir(obj: Venda) -> None:
        x = VendaDAO.listar_id(obj.id)
        if x != None:
            VendaDAO.objetos.remove(x)
            VendaDAO.salvar()
            
    @staticmethod
    def converte_str(o):
        if isinstance(o, datetime):
            return o.isoformat()
        return vars(o)

    @staticmethod
    def salvar() -> None:
        with open("vendas.json", mode = "w") as arquivo:
            json.dump(VendaDAO.objetos, arquivo, default = VendaDAO.converte_str)

    @staticmethod
    def abrir() -> None:
        VendaDAO.objetos = []
        try:
            with open("vendas.json", mode = "r") as arquivo:
                vendas_json = json.load(arquivo)
                for obj in vendas_json:
                    v = Venda(obj["id"], datetime.fromisoformat(obj["data"]), obj["carrinho"], obj["total"], obj["idCliente"])
                    VendaDAO.objetos.append(v)
        except FileNotFoundError:
            VendaDAO.objetos = []