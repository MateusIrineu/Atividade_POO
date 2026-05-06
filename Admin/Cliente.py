import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    
class ClienteDAO:
    objetos = []
    @staticmethod
    def inserir(obj):
        ClienteDAO.abrir()
        if len(ClienteDAO.objetos) == 0: 
            id = 1

        else: 
            id = (max(ClienteDAO.objetos, key = lambda x : x.id)).id + 1

        obj.id = id
        ClienteDAO.objetos.append(obj)
        ClienteDAO.salvar()

    @staticmethod
    def listar():
        ClienteDAO.abrir()
        ClienteDAO.objetos.sort(key = lambda x : x.nome)
        return ClienteDAO.objetos
    
    @staticmethod
    def listar_id(id):
        ClienteDAO.abrir()
        for obj in ClienteDAO.objetos:
            if obj.id == id: 
                return obj
        return None
       
    @staticmethod
    def atualizar(obj):
        x = ClienteDAO.listar_id(obj.id)
        if x != None:
            ClienteDAO.objetos.remove(x)
            ClienteDAO.objetos.append(obj)
            ClienteDAO.salvar()

    @staticmethod
    def excluir(obj):
        x = ClienteDAO.listar_id(obj.id)
        if x != None:
            ClienteDAO.objetos.remove(x)
            ClienteDAO.salvar()

    @staticmethod
    def salvar():
        with open("clientes.json", mode="w") as arquivo:
            json.dump(ClienteDAO.objetos, arquivo, default = vars)  
                           
    @staticmethod
    def abrir():
        ClienteDAO.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    ClienteDAO.objetos.append(c)        
        except FileNotFoundError:
            ClienteDAO.objetos = []