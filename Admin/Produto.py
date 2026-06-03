import json
# vou utilizar tipado esse arquivo por fins de estudo
class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int, idCategoria: int, imagem: str ):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
        self.imagem = imagem

    def __str__(self) -> str:
        return f" #{self.id} - Nome: {self.descricao} - Preço: R$ {self.preco} - Estoque: {self.estoque} - id da Categoria: #{self.idCategoria} - imagem: {self.imagem}"
    
    def to_dict(self):
        return {"Id":self.id,"Nome": self.descricao, "Preço": self.preco, "Estoque": self.estoque, "idCategoria": self.idCategoria, "Imagem": f"data:image/png;base64,{self.imagem}" if self.imagem else None}
    
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

    def alterar_preco_geral(self, percentual: float) -> None:

        self.abrir()
        for produto in self.objetos:
            produto.preco = round(produto.preco * (1 + percentual / 100), 2)
        self.salvar()

    def salvar(self) -> None:
        with open("Jsons/produtos.json", mode = "w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)

    def abrir(self) -> None:
        self.objetos = []
        try:
            with open("Jsons/produtos.json", mode = "r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    p = Produto(obj["id"], obj["descricao"], obj["preco"], obj["estoque"], obj["idCategoria"], obj["imagem"])
                    self.objetos.append(p)
        except FileNotFoundError:
            self.objetos = []

    