from Cliente.View import View as ClienteView
from Visitante.Login import LoginDAO
import streamlit as st
from streamlit_option_menu import option_menu
import time


class ClienteInterface:
    @staticmethod
    def main() -> None:

        st.session_state.email_logado
        st.session_state.nome_cliente_logado

        with st.sidebar:
            st.info(f"Bem Vindo, {st.session_state.nome_cliente_logado}")

            aba_selecionada = option_menu(
                menu_title = "Painel Cliente",
                options = ["Ver Produtos", "Meu Carrinho", "Finalizar Compra", "Meus Pedidos"],
                icons = ["box-seam", "cart", "cash-coin", "receipt"],
                default_index = 0,
                key = "cliente_menu"
            )
            button_sair: bool = st.button("Sair", type="primary")
            if button_sair:
                ClienteInterface.sair()

        if aba_selecionada == "Ver Produtos":
            ClienteInterface.produto_listar()

        elif aba_selecionada == "Meu Carrinho":
            ClienteInterface.meu_carrinho()

        elif aba_selecionada == "Finalizar Compra":
            ClienteInterface.finalizar_compra()

        elif aba_selecionada == "Meus Pedidos":
            ClienteInterface.ver_pedidos()
        
    #Ver Produtos da Loja
    @staticmethod
    def produto_listar()-> None:
        st.header("Listagem de Produtos", divider="blue")
        with st.container(border=True):
            st.subheader("Produtos Disponiveis")
            for p in ClienteView.listar_produtos():
                st.text(p)

    #Ver carrinho e adicionar produto no carrinho
    @staticmethod
    def meu_carrinho()-> None:
        st.header("Meu Carrinho", divider="red")
        aba1, aba2 = st.tabs(["Ver Carrinho", "Adicionar Produto"])
        # aba3 = "Limpar Carrinho"
        with aba1:
            with st.container(border=True):
                for c in ClienteView.visualizar_carrinho(st.session_state.id_cliente_logado):
                    st.text(c)
            if st.button("Limpar Carrinho"):
                ClienteView.limpar_carrinho(st.session_state.id_cliente_logado)
                st.success("Carrinho limpo!")
                time.sleep(2)
                st.rerun()

        with aba2:
            idProduto = st.number_input("Informe o ID do produto: ", min_value=1)
            quantidade = st.number_input("Informe a quantidade: ", min_value=1)
            if st.button("Adicionar ao Carrinho"):
                if ClienteView.inserir_produto_carrinho(st.session_state.id_cliente_logado, idProduto, quantidade):
                    st.success("Produto adicionado ao carrinho!")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Produto não encontrado!")

        # with aba3:
        #     with st.container(border=True):
        #         for c in ClienteView.visualizar_carrinho(LoginDAO.idCliente_logado):
        #             st.text(c)
        #     if st.button("Limpar Carrinho"):
        #         ClienteView.limpar_carrinho(LoginDAO.idCliente_logado)
        #         st.success("Carrinho limpo!")
                

    #Finalizar Pedido
    @staticmethod
    def finalizar_compra()-> None:
        st.header("Finalizar Pedido", divider="green")
        with st.container(border=True):
            st.subheader("Meu Carrinho")
            for c in ClienteView.visualizar_carrinho(st.session_state.id_cliente_logado):
                st.text(c)
        if st.button("Confirmar Compra"):
            if ClienteView.comprar_carrinho(st.session_state.id_cliente_logado):
                st.success("Compra realizada com sucesso!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Carrinho vazio!")
    
    @staticmethod
    def ver_pedidos()-> None:
        st.header("Minhas Compras", divider="green")
        with st.container(border=True):
            for p in ClienteView.listar_compras(st.session_state.id_cliente_logado):
                st.text(p)

    @staticmethod
    def sair() -> None:
        st.session_state.usuario_logado = False
        st.session_state.email_logado = None
        st.rerun()








# class ClienteUI:
#     #TELA DE ACESSO DO CLIENTE
#     @staticmethod
#     def cliente_main():
#         op = 0
#         while True:
#             op = ClienteUI.cliente_menu()
#             if op == 1: ClienteUI.inserir_produto()
#             if op == 2: ClienteUI.listar_produtos()
#             if op == 3: ClienteUI.listar_compras()
#             if op == 4: ClienteUI.visualizar_carrinho()
#             if op == 5: ClienteUI.comprar_carrinho()
#             if op == 6: ClienteUI.limpar_carrinho()
#             if op == 7: ClienteUI.sair()

#     @staticmethod
#     def sair():
#         from UI import UI
#         UI.validacao()

#     #MENU CLIENTE
#     @staticmethod
#     def cliente_menu():
#         print("1 - Inserir produto")
#         print("2 - Listar produtos")
#         print("3 - Listar Compras")
#         print("4 - Visualizar Carrinho")
#         print("5 - Comprar Carrinho")
#         print("6 - Limpar Carrinho")
#         print("7 - Sair do Sistema")
#         return int(input("Informe uma opção: "))

# # CLIENTE (CARRINHO E COMPRAS)
#     @staticmethod
#     def listar_produtos():
#         print("Listagem de Produtos Disponíveis")
#         for p in ClienteView.listar_produtos():
#             print(p)

#     @staticmethod
#     def inserir_produto():
#         ClienteUI.listar_produtos()
#         idProduto = int(input("Insira o id do produto a adicionar: "))
#         quantidade = int(input("Informe a quantidade: "))
#         if ClienteView.inserir_produto_carrinho(LoginDAO.idCliente_logado, idProduto, quantidade):
#             print("Produto adicionado ao carrinho!")
#         else:
#             print("Produto não encontrado!")

#     @staticmethod
#     def visualizar_carrinho():
#         print("Itens do Carrinho")
#         itens = ClienteView.visualizar_carrinho(LoginDAO.idCliente_logado)
#         if len(itens) == 0:
#             print("Carrinho vazio!")
#         else:
#             for item in itens:
#                 print(item)

#     @staticmethod
#     def comprar_carrinho():
#         if ClienteView.comprar_carrinho(LoginDAO.idCliente_logado):
#             print("Compra realizada com sucesso!")
#         else:
#             print("Carrinho vazio!")

#     @staticmethod
#     def listar_compras():
#         print("Histórico de Compras")
#         compras = ClienteView.listar_compras(LoginDAO.idCliente_logado)
#         if len(compras) == 0:
#             print("Nenhuma compra realizada!")
#         else:
#             for compra in compras:
#                 print(compra)

# #FUNÇÃO ADICIONAL
#     @staticmethod
#     def limpar_carrinho():
#         ClienteView.limpar_carrinho(LoginDAO.idCliente_logado)
#         print("Carrinho limpo!")
