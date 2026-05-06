import json
# vou utilizar tipado esse arquivo por fins de estudo
class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int, idCategoria: int ):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
    def __str__(self) -> str:
        return f"{self.id} - {self.descricao} - {self.preco} - {self.estoque} - {self.idCategoria}"
    
class ProdutoDAO:
    def __init__(self):
        self.objetos: list[Produto] = []

    def inserir(self, obj: Produto) -> None:
        self.abrir()
        if len(self.objetos) == 0:
            id = 1
        else:
            id = (max(self.objetos, key = lambda x : x.id)).id + 1
        obj.id = id
        self.objetos.append(obj)
        self.salvar()
    
    def listar(self) -> list[Produto]:
        self.abrir()
        self.objetos.sort(key = lambda x : x.descricao)
        return self.objetos
    
    def listar_id(self, id: int) -> Produto | None:
        self.abrir()
        for obj in self.objetos:
            if obj.id == id:
                return obj
        return None
    
    def atualizar(self, obj: Produto) -> None:
        x = self.listar_id(obj.id)
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()

    def excluir(self, obj: Produto) -> None:
        x = self.listar_id(obj.id)
        if x != None:
            self.objetos.remove(x)
            self.salvar()

    def salvar(self) -> None:
        with open("produtos.json", mode = "w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)

    def abrir(self) -> None:
        self.objetos = []
        try:
            with open("produtos.json", mode = "r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    p = Produto(obj["id"], obj["descricao"], obj["preco"], obj["estoque"], obj["idCategoria"])
                    self.objetos.append(p)
        except FileNotFoundError:
            self.objetos = []