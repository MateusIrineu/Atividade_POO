import json
from datetime import date
from Admin.Crud import CRUD

class Promocao:
    def __init__(self, id: int, idCategoria: int, percentual: float, inicio: str, fim: str):
        self.id = id
        self.idCategoria = idCategoria
        self.percentual = percentual
        self.inicio = inicio  # formato "YYYY-MM-DD"
        self.fim = fim        # formato "YYYY-MM-DD"

    def __str__(self):
        return f"#{self.id} - Categoria #{self.idCategoria} - {self.percentual}% de {self.inicio} até {self.fim}"

    def esta_ativa(self) -> bool:
        hoje = date.today().isoformat()
        return self.inicio <= hoje <= self.fim

    def to_dict(self):
        return {
            "Id": self.id,
            "idCategoria": self.idCategoria,
            "Desconto (%)": self.percentual,
            "Início": self.inicio,
            "Fim": self.fim,
            "Ativa": "Sim" if self.esta_ativa() else "Não"
        }


class PromocaoDAO(CRUD):
    objetos: list[Promocao] = []

    @classmethod
    def salvar(cls):
        with open("Jsons/promocoes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Jsons/promocoes.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    p = Promocao(obj["id"], obj["idCategoria"], obj["percentual"], obj["inicio"], obj["fim"])
                    cls.objetos.append(p)
        except FileNotFoundError:
            cls.objetos = []

    @classmethod
    def obter_desconto_categoria(cls, idCategoria: int) -> float:
        """Retorna o percentual de desconto ativo para a categoria, ou 0 se não houver."""
        cls.abrir()
        hoje = date.today().isoformat()
        for promo in cls.objetos:
            if promo.idCategoria == idCategoria and promo.inicio <= hoje <= promo.fim:
                return promo.percentual
        return 0.0
