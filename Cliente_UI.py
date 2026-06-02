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
                options = ["Ver Produtos", "Carrinho", "Meus Pedidos"],
                icons = ["box-seam", "cart", "cash-coin", "receipt"],
                default_index = 0,
                key = "cliente_menu"
            )
            button_sair: bool = st.button("Sair", type="primary")
            if button_sair:
                ClienteInterface.sair()

        if aba_selecionada == "Ver Produtos":
            ClienteInterface.produto_listar()

        elif aba_selecionada == "Carrinho":
            ClienteInterface.meu_carrinho()

        elif aba_selecionada == "Meus Pedidos":
            ClienteInterface.ver_pedidos()
        
    #VER PRODUTOS E ADICIONAR AO CARRINHO
    @staticmethod
    def produto_listar()-> None:
        st.header("Listagem de Produtos", divider="blue")
        try:
            with st.container(border=True):
                st.subheader("Produtos Disponiveis")
                for p in ClienteView.listar_produtos():
                    st.dataframe([p.to_dict()])

        except ValueError as erro:
            print(" ---- Erro ---->", erro)

        try:
            with st.container(border=True):
                    st.subheader("Adicionar Produtos")
                    idProduto = st.number_input("Informe o ID do produto: ", min_value=1)
                    quantidade = st.number_input("Informe a quantidade: ", min_value=1)
                    if st.button("Adicionar ao Carrinho"):
                        try:
                            if ClienteView.inserir_produto_carrinho(st.session_state.id_cliente_logado, idProduto, quantidade):
                                st.success("Produto adicionado ao carrinho!")
                                time.sleep(2)
                                st.rerun()
                            else:
                                st.error("Produto não encontrado!")
                        except ValueError as erro:
                            print(" ---- Erro ---->", erro)
        except ValueError as erro:
            print(" ---- Erro ---->", erro)

    #VER CARRINHO E FINALIZAR COMPRA
    @staticmethod
    def meu_carrinho()-> None:
        st.header("Carrinho", divider="red")
        
        if ClienteView.visualizar_carrinho(st.session_state.id_cliente_logado): 
            with st.container(border=True):
                for c in ClienteView.visualizar_carrinho(st.session_state.id_cliente_logado):
                    st.dataframe([c.to_dict()])
            if st.button("Limpar Carrinho"):
                ClienteView.limpar_carrinho(st.session_state.id_cliente_logado)
                st.success("Carrinho limpo!")
                time.sleep(2)
                st.rerun()

            if st.button("Confirmar Compra"):
                    if ClienteView.comprar_carrinho(st.session_state.id_cliente_logado):
                        st.success("Compra realizada com sucesso!")
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.error("Carrinho vazio!")
        else:
            st.info("Seu Carrinho esta vazio no momento!!")
    
    @staticmethod
    def ver_pedidos()-> None:
        st.header("Historico de Compras", divider="green")
        try:   
            with st.container(border=True):
                for p in ClienteView.listar_compras(st.session_state.id_cliente_logado):
                    st.dataframe([p.to_dict()])

        except ValueError as erro:
            print(" ---- Erro ---->", erro)

    @staticmethod
    def sair() -> None:
        st.session_state.usuario_logado = False
        st.session_state.email_logado = None
        st.rerun()
