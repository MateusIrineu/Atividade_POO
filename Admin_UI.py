from Admin.View import View as AdminView
import streamlit as st
from streamlit_option_menu import option_menu

class AdminUI:
    #TELA DE ACESSO DO ADMIN
    @staticmethod
    def main():

        email_admin = st.session_state.email_logado

        with st.sidebar:
            st.info(f"Bem vindo, {st.session_state.email_logado}")


            aba_selecionada = option_menu(
                menu_title = "Painel Admin",
                options = ["Clientes", "Categorias", "Produtos"],
                icons = ["people", "tags", "box-seam" ],
                default_index = 0
            )
            button_sair: bool = st.button("Sair", type="primary")
            if button_sair:
                AdminUI.sair()

        if aba_selecionada == "Clientes":
            st.header("Gerenciamento de Clientes", divider="blue")
            resposta: str = st.radio("Escolha a opção:", ["Inserir cliente", "Listar clientes", "Atualizar cliente", "Excluir cliente"])

            if resposta == "Inserir cliente":
                AdminUI.cliente_inserir()
            elif resposta == "Listar clientes":
                AdminUI.cliente_listar()
            elif resposta == "Atualizar cliente":
                AdminUI.cliente_atualizar()
            elif resposta == "Excluir cliente":
                AdminUI.cliente_excluir()

        if aba_selecionada == "Categorias":
            st.header("Gerenciamento de Categorias", divider="red")
            resposta: str = st.radio("Escolha a opção:", ["Inserir categoria", "Listar categorias", "Atualizar categoiria", "Excluir categoria"])

            if resposta == "Inserir categoria":
                AdminUI.categoria_inserir()
            elif resposta == "Listar categorias":
                AdminUI.categoria_listar()
            elif resposta == "Atualizar categoiria":
                AdminUI.categoria_atualizar()
            elif resposta == "Excluir categoria":
                AdminUI.categoria_excluir()

        if aba_selecionada == "Produtos":
            st.header("Gerenciamento de Produtos", divider="green")
            resposta: str = st.radio("Escolha a opção:", ["Inserir produto", "Listar produtos", "Atualizar produto", "Excluir produto", "Alterar preço"])

            if resposta == "Inserir produto":
                AdminUI.produto_inserir()
            elif resposta == "Listar produtos":
                AdminUI.produto_listar()
            elif resposta == "Atualizar produto":
                AdminUI.produto_atualizar()
            elif resposta == "Excluir produto":
                AdminUI.produto_excluir()
            elif resposta == "Alterar preço":
                AdminUI.produto_alterar_preco_geral()

    @staticmethod
    def sair():
        from UI import UI
        st.session_state.usuario_logado = False
        st.session_state.email_logado = None
        st.rerun()

    #MENU ADMIN
    # @staticmethod
    # def menu():
    #     print("----- Clientes -----")
    #     print("1 - Inserir 2 - Listar 3 - Atualizar 4 - Excluir")
    #     print("----------------------------------------")
    #     print("----- Categorias -----")
    #     print("5 - Inserir 6 - Listar 7 - Atualizar 8 - Excluir")
    #     print("----------------------------------------")
    #     print("----- Produtos -----")
    #     print("9 - Inserir 10 - Listar 11 - Atualizar 12 - Excluir 13 - Alterar Preço Geral")
    #     print("----------------------------------------")
    #     print("14 - Sair do sistema")
    #     return int(input("Informe uma opção: "))

#CLIENTE POR ADMIN
    @staticmethod
    def cliente_inserir():
        print("Cadastro de Clientes")
        with st.form("form_inserir_cliente"):
            nome: str = st.text_input("Informe o nome: ")
            email: str = st.text_input("Informe o e-mail: ")
            senha: str = st.text_input("Informe a senha: ")
            fone: str = st.text_input("Informe o fone: ")

            submit: bool = st.form_submit_button("Inserir Cliente", type="secondary")
    
        if submit:
            AdminView.cliente_inserir(nome, email, senha, fone)
            st.success("Cliente inserido com sucesso!")

    @staticmethod
    def cliente_listar():
        st.text("Listagem de Clientes")
        for c in AdminView.cliente_listar():
            st.text(c)

    @staticmethod
    def cliente_atualizar():
        AdminUI.cliente_listar()
        with st.form("form_atualizar_cliente"):
            id: int = int(st.text_input("Qual o id do cliente a ser atualizado: ", value=1, key="upd_id"))
            nome: str = st.text_input("Informe o novo nome: ", key="upd_nome")
            email: str = st.text_input("Informe o novo e-mail: ", key="upd_email")
            senha: str = st.text_input("Informe a nova senha: ", key="upd_senha")
            fone: str = st.text_input("Informe o novo fone: ", key="upd_fone")
            submit: bool = st.form_submit_button("Atualizar Cliente", type="secondary")

        if submit:
            AdminView.cliente_atualizar(id, nome, email, senha, fone)
            st.success("Cliente atualizado com sucesso!")
            st.rerun()

    @staticmethod
    def cliente_excluir():
        AdminUI.cliente_listar()
        with st.form("form_excluir_cliente"):
            id: int = int(st.text_input("Qual o id do cliente a ser excluído: ", value=1))
            submit: bool = st.form_submit_button("Excluir cliente", type="secondary")

        if submit:
            AdminView.cliente_excluir(id)
            st.success("Cliente excluído com sucesso.")

#CATEGORIA POR ADMIN
    @staticmethod
    def categoria_inserir():
        print("Cadastro de Categorias")
        desc = input("Informe a descrição: ")
        # c = Categoria(0, desc)
        AdminView.categoria_inserir(desc)

    @staticmethod
    def categoria_listar():
        print("Listagem de Categorias")
        for c in AdminView.categoria_listar():
            print(c)

    @staticmethod
    def categoria_atualizar():
        AdminUI.categoria_listar()
        id = int(input("Qual o id da categoria a ser atualizado: "))
        desc = input("Informe a nova descrição: ")
        # c = Categoria(id, desc)
        AdminView.categoria_atualizar(id, desc)

    @staticmethod
    def categoria_excluir():
        AdminUI.categoria_listar()
        id = int(input("Qual o id da categoria a ser excluído: "))
        # c = Categoria(id, "")
        AdminView.categoria_excluir(id)

# PRODUTO POR ADMIN
    @staticmethod
    def produto_inserir():
        print("Cadastro de Produtos")
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        idCategoria = int(input("Insira a categoria do produto: "))
        # p = Produto(0, descricao, preco, estoque, idCategoria)
        AdminView.produto_inserir(descricao, preco, estoque, idCategoria)

    @staticmethod
    def produto_listar():
        print("Listagem de Produtos")
        for p in AdminView.produto_listar():
            print(p)

    @staticmethod
    def produto_atualizar():
        AdminUI.produto_listar()
        id = int(input("Insira o id do produto a ser atualizado: "))
        descricao = input("Insira a nova descrição: ")
        preco = float(input("Insira o novo preço: "))
        estoque = int(input("Insira a nova quantidade em estoque: "))
        idCategoria = int(input("Insira o id da nova categoria do produto: "))
        # p = Produto(id, descricao, preco, estoque, idCategoria)
        AdminView.produto_atualizar(id, descricao, preco, estoque, idCategoria)

    @staticmethod
    def produto_excluir():
        AdminUI.produto_listar()
        id = int(input("Insira o id do produto a ser excluído: "))
        # p = Produto(id, "", 0.0, 0, 0)
        AdminView.produto_excluir(id)

    @staticmethod
    def produto_alterar_preco_geral():
        percentual = float(input("Insira o percentual de alteracao (ex: 10 para +10%, -5 para -5%): "))
        AdminView.produto_alterar_preco_geral(percentual)
        print("Precos alterados com sucesso!")
