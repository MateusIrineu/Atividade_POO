from Cliente.View import View as ClienteView
from Visitante.Login import LoginDAO


class ClienteUI:
    #TELA DE ACESSO DO CLIENTE
    @staticmethod
    def cliente_main():
        op = 0
        while True:
            op = ClienteUI.cliente_menu()
            if op == 1: ClienteUI.inserir_produto()
            if op == 2: ClienteUI.listar_produtos()
            if op == 3: ClienteUI.listar_compras()
            if op == 4: ClienteUI.visualizar_carrinho()
            if op == 5: ClienteUI.comprar_carrinho()
            if op == 6: ClienteUI.limpar_carrinho()
            if op == 7: ClienteUI.sair()

    @staticmethod
    def sair():
        from UI import UI
        UI.validacao()

    #MENU CLIENTE
    @staticmethod
    def cliente_menu():
        print("1 - Inserir produto")
        print("2 - Listar produtos")
        print("3 - Listar Compras")
        print("4 - Visualizar Carrinho")
        print("5 - Comprar Carrinho")
        print("6 - Limpar Carrinho")
        print("7 - Sair do Sistema")
        return int(input("Informe uma opção: "))

# CLIENTE (CARRINHO E COMPRAS)
    @staticmethod
    def listar_produtos():
        print("Listagem de Produtos Disponíveis")
        for p in ClienteView.listar_produtos():
            print(p)

    @staticmethod
    def inserir_produto():
        ClienteUI.listar_produtos()
        idProduto = int(input("Insira o id do produto a adicionar: "))
        quantidade = int(input("Informe a quantidade: "))
        if ClienteView.inserir_produto_carrinho(LoginDAO.idCliente_logado, idProduto, quantidade):
            print("Produto adicionado ao carrinho!")
        else:
            print("Produto não encontrado!")

    @staticmethod
    def visualizar_carrinho():
        print("Itens do Carrinho")
        itens = ClienteView.visualizar_carrinho(LoginDAO.idCliente_logado)
        if len(itens) == 0:
            print("Carrinho vazio!")
        else:
            for item in itens:
                print(item)

    @staticmethod
    def comprar_carrinho():
        if ClienteView.comprar_carrinho(LoginDAO.idCliente_logado):
            print("Compra realizada com sucesso!")
        else:
            print("Carrinho vazio!")

    @staticmethod
    def listar_compras():
        print("Histórico de Compras")
        compras = ClienteView.listar_compras(LoginDAO.idCliente_logado)
        if len(compras) == 0:
            print("Nenhuma compra realizada!")
        else:
            for compra in compras:
                print(compra)

#FUNÇÃO ADICIONAL
    @staticmethod
    def limpar_carrinho():
        ClienteView.limpar_carrinho(LoginDAO.idCliente_logado)
        print("Carrinho limpo!")
