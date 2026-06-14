import json
from datetime import datetime
from Admin.Cliente import Cliente, ClienteDAO
from Admin.Crud import CRUD
from Admin.Entregador import EntregadorDAO  # Importamos o novo DAO

class Venda:
    # Atualizado com status_entrega e idEntregador default
    def __init__(self, id: int, data: datetime, carrinho: bool, total: float, idCliente: int, status_entrega: str = "Pendente", idEntregador: int = 0):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.idCliente = idCliente
        self.status_entrega = status_entrega
        self.idEntregador = idEntregador
    
    def __str__(self) -> str:
        data_formatada = self.data.strftime("%d/%m/%Y - Horário: %H:%M:%S")
        cliente = ClienteDAO.listar_id(self.idCliente)
        nome = cliente.nome if cliente else "Desconhecido"
        return f"ID Compra: #{self.id} - Data: {data_formatada} - Total: R$ {self.total} - Cliente: {nome} - Status: {self.status_entrega}"
    
    def to_dict(self):
        data_formatada = self.data.strftime("%d/%m/%Y - Horário: %H:%M:%S")
        cliente = ClienteDAO.listar_id(self.idCliente)
        nome = cliente.nome if cliente else "Desconhecido"
        
        # Recupera nome do entregador se houver um associado
        entregador = EntregadorDAO.listar_id(self.idEntregador) if self.idEntregador > 0 else None
        nome_entregador = entregador.nome if entregador else "Não alocado"
        
        return {
            "ID Compra": self.id, 
            "Data": data_formatada,
            "Total": self.total, 
            "Cliente": nome,
            "Status Entrega": self.status_entrega,
            "Entregador": nome_entregador
        }
    
class VendaDAO(CRUD):
    objetos: list[Venda] = []
            
    @staticmethod
    def converte_str(o):
        if isinstance(o, datetime):
            return o.isoformat()
        return vars(o)

    @classmethod
    def salvar(cls) -> None:
        with open("Jsons/vendas.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = cls.converte_str)

    @classmethod
    def abrir(cls) -> None:
        cls.objetos = []
        try:
            with open("Jsons/vendas.json", mode = "r") as arquivo:
                vendas_json = json.load(arquivo)
                for obj in vendas_json:
                    # Lemos os novos campos tratando compatibilidade caso chaves antigas não existam no json
                    status = obj.get("status_entrega", "Pendente")
                    entregador_id = obj.get("idEntregador", 0)
                    v = Venda(obj["id"], datetime.fromisoformat(obj["data"]), obj["carrinho"], obj["total"], obj["idCliente"], status, entregador_id)
                    cls.objetos.append(v)
        except FileNotFoundError:
            cls.objetos = []