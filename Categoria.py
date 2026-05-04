import json

class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"
    
class CategoriaDAO:
    def __init__(self):
        self.objetos = []

    def inserir(self, obj):
        self.abrir()
        if len(self.objetos) == 0: 
            id = 1
        else: 
            id = (max(self.objetos, key = lambda x : x.id)).id + 1
        obj.id = id
        self.objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        self.objetos.sort(key = lambda x : x.descricao)
        return self.objetos
    
    def listar_id(self, id):
        self.abrir()
        for obj in self.objetos:
            if obj.id == id: 
                return obj
        return None    
        
    def atualizar(self, obj):
        x = self.listar_id(obj.id)
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()

    def excluir(self, obj):
        x = self.listar_id(obj.id)
        if x != None:
            self.objetos.remove(x)
            self.salvar()

    def salvar(self):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)
                         
    def abrir(self):
        self.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    c = Categoria(obj["id"], obj["descricao"])
                    self.objetos.append(c)        
        except FileNotFoundError:
            self.objetos = []