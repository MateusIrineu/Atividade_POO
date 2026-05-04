import json

class VendaItem:
	def __init__(self, id: int, qtd: int, preco: float, idVenda: int, idProduto: int):
		self.id = id
		self.qtd = qtd
		self.preco = preco
		self.idVenda = idVenda
		self.idProduto = idProduto

	def __str__(self) -> str:
		return f"{self.id} - {self.qtd} - {self.preco} - {self.idVenda} - {self.idProduto}"

class VendaItemDAO:
	objetos: list[VendaItem] = []

	@staticmethod
	def inserir(obj: VendaItem) -> None:
		VendaItemDAO.abrir()
		if len(VendaItemDAO.objetos) == 0:
			id = 1
		else:
			id = (max(VendaItemDAO.objetos, key = lambda x : x.id)).id + 1
		obj.id = id
		VendaItemDAO.objetos.append(obj)
		VendaItemDAO.salvar()

	@staticmethod
	def listar() -> list[VendaItem]:
		VendaItemDAO.abrir()
		VendaItemDAO.objetos.sort(key = lambda x : x.id)
		return VendaItemDAO.objetos

	@staticmethod
	def listar_id(id: int) -> VendaItem | None:
		VendaItemDAO.abrir()
		for obj in VendaItemDAO.objetos:
			if obj.id == id:
				return obj
		return None

	@staticmethod
	def atualizar(obj: VendaItem) -> None:
		x = VendaItemDAO.listar_id(obj.id)
		if x != None:
			VendaItemDAO.objetos.remove(x)
			VendaItemDAO.objetos.append(obj)
			VendaItemDAO.salvar()

	@staticmethod
	def excluir(obj: VendaItem) -> None:
		x = VendaItemDAO.listar_id(obj.id)
		if x != None:
			VendaItemDAO.objetos.remove(x)
			VendaItemDAO.salvar()

	@staticmethod
	def salvar() -> None:
		with open("vendaitens.json", mode = "w") as arquivo:
			json.dump(VendaItemDAO.objetos, arquivo, default = vars)

	@staticmethod
	def abrir() -> None:
		VendaItemDAO.objetos = []
		try:
			with open("vendaitens.json", mode = "r") as arquivo:
				objetos_json = json.load(arquivo)
				for obj in objetos_json:
					vi = VendaItem(obj["id"], obj["qtd"], obj["preco"], obj["idVenda"], obj["idProduto"])
					VendaItemDAO.objetos.append(vi)
		except FileNotFoundError:
			VendaItemDAO.objetos = []
