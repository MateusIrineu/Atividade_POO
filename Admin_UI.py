from Admin.View import View as AdminView
import streamlit as st
from streamlit_option_menu import option_menu
import time

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
                default_index = 0,
                key = "admin_menu"
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
        st.session_state.usuario_logado = False
        st.session_state.email_logado = None
        st.rerun()

#CLIENTE POR ADMIN
    @staticmethod
    def cliente_inserir():
        with st.form("form_inserir_cliente"):
            st.subheader("Cadastro de Clientes")
            nome: str = st.text_input("Informe o nome: ")
            email: str = st.text_input("Informe o e-mail: ")
            senha: str = st.text_input("Informe a senha: ")
            fone: str = st.text_input("Informe o fone: ")

            submit: bool = st.form_submit_button("Inserir Cliente", type="secondary")
    
        if submit:
            AdminView.cliente_inserir(nome, email, senha, fone)
            st.success("Cliente inserido com sucesso!")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def cliente_listar():
        with st.container(border=True):
            st.subheader("Listagem de Clientes")
            for c in AdminView.cliente_listar():
                st.text(c)

    @staticmethod
    def cliente_atualizar():
        with st.form("form_atualizar_cliente"):
            AdminUI.cliente_listar()
            st.subheader("Atualização de Cliente")
            id_str: str = st.text_input("Qual o id do cliente a ser atualizado: ", value=1) or ''
            id: int = int(id_str) if id_str.isdigit() else 0
            nome: str = st.text_input("Informe o novo nome: ")
            email: str = st.text_input("Informe o novo e-mail: ")
            senha: str = st.text_input("Informe a nova senha: ")
            fone: str = st.text_input("Informe o novo fone: ")
            submit: bool = st.form_submit_button("Atualizar Cliente", type="secondary")

        if submit:
            AdminView.cliente_atualizar(id, nome, email, senha, fone)
            st.success("Cliente atualizado com sucesso!")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def cliente_excluir():
        with st.form("form_excluir_cliente"):
            AdminUI.cliente_listar()
            st.subheader("Exclusão de Cliente")
            id_str: str = st.text_input("Qual o id do cliente a ser excluído: ", value=1) or ''
            id: int = int(id_str) if id_str.isdigit() else 0
            submit: bool = st.form_submit_button("Excluir cliente", type="secondary")         

        if submit:
            AdminView.cliente_excluir(id)
            st.success("Cliente excluído com sucesso!")
            time.sleep(2)
            st.rerun()

#CATEGORIA POR ADMIN
    @staticmethod
    def categoria_inserir():
        with st.form("form_inserir_categoria"):
            st.subheader("Cadastro de Categorias")
            desc: str = st.text_input("Informe a descrição: ")

            submit: bool = st.form_submit_button("Inserir Categoria", type="secondary")

        if submit:
            AdminView.categoria_inserir(desc)
            st.success("Categoria inserida com sucesso!")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def categoria_listar():
       with st.container(border=True):
            st.subheader("Listagem de Categorias")
            for c in AdminView.categoria_listar():
                st.text(c)

    @staticmethod
    def categoria_atualizar():
        with st.form("form_atualizar_categoria"):
            AdminUI.categoria_listar()
            st.subheader("Atualização de Cliente")

            id_str: str = st.text_input("Qual o id da categoria a ser atualizado: ", value=1) or ''
            id: int = int(id_str) if id_str.isdigit() else 0

            desc: str = st.text_input("Informe a nova descrição: ")
            submit: bool = st.form_submit_button("Atualizar categoria", type="secondary")

        if submit:
            AdminView.categoria_atualizar(id, desc)
            st.success("Categoria atualizada com sucesso!")
            time.sleep(2)
            st.rerun()
            

    @staticmethod
    def categoria_excluir():
        with st.form("form_excluir_categoria"):
            AdminUI.categoria_listar()
            st.subheader("Exclusão de Categoria")

            id_str = st.text_input("Qual o id da categoria a ser excluído: ", value=1) or ''
            id = int(id_str) if id_str.isdigit() else 0

            submit: bool = st.form_submit_button("Excluir categoria", type="secondary")

        if submit:
            AdminView.categoria_excluir(id)
            st.success("Categoria excluída com sucesso!")
            time.sleep(2)
            st.rerun()

# PRODUTO POR ADMIN
    @staticmethod
    def produto_inserir():
        with st.form("form_inserir_produto"):
            st.subheader("Cadastro de Produtos")
            descricao: str = st.text_input("Informe a descrição: ")

            preco_str: str = st.text_input("Informe o preço: ", value=1.0) or ''
            try:
                preco: float = float(preco_str.replace(",", "."))
            except ValueError:
                preco = 0.0

            estoque_str: str = st.text_input("Informe a quantidade em estoque: ", value=1) or ''
            estoque = int(estoque_str) if estoque_str.isdigit() else 0

            idCategoria_str: str = st.text_input("Insira a categoria do produto: ", value=1) or ''
            idCategoria = int(idCategoria_str) if idCategoria_str.isdigit() else 0
        
            submit: bool = st.form_submit_button("Inserir produto", type="secondary")
            
        if submit:
            AdminView.produto_inserir(descricao, preco, estoque, idCategoria)
            st.success("Produto inserido com sucesso!")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def produto_listar():
        with st.container(border=True):
            st.subheader("Listagem de Produtos")
            for p in AdminView.produto_listar():
                st.text(p)

    @staticmethod
    def produto_atualizar():
        with st.form("form_atualizar_produto"):
            AdminUI.produto_listar()
            st.subheader("Atualização de Produto")

            id_str: str = st.text_input("Insira o id do produto a ser atualizado: ", value=1) or ''
            id: int = int(id_str) if id_str.isdigit() else 0

            descricao: str = st.text_input("Insira a nova descrição: ")

            preco_str: str = st.text_input("Insira o novo preço: ", value=1.0) or ''
            try:
                preco: float = float(preco_str.replace(",", "."))
            except ValueError:
                preco = 0.0

            estoque_str: str = st.text_input("Insira a nova quantidade em estoque: ", value=1) or ''   
            estoque = int(estoque_str) if estoque_str.isdigit() else 0

            idCategoria_str: str = st.text_input("Insira o id da nova categoria do produto: ", value=1) or ''
            idCategoria = int(idCategoria_str) if idCategoria_str.isdigit() else 0

            submit: bool = st.form_submit_button("Atualizar produto", type="secondary")

        if submit:
            AdminView.produto_atualizar(id, descricao, preco, estoque, idCategoria)
            st.success("Produto atualizado com sucesso!")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def produto_excluir():
        with st.form("form_excluir_produto"):
            AdminUI.produto_listar()
            st.subheader("Exclusão de Produto")

            id_str: str = st.text_input("Insira o id do produto a ser excluído: ", value=1) or ''
            id = int(id_str) if id_str.isdigit else 0
        
            submit: bool = st.form_submit_button("Excluir produto", type="secondary")

        if submit:
            AdminView.produto_excluir(id)
            st.success("Produto excluído com sucesso!")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def produto_alterar_preco_geral():
        with st.form("form_alterar_preco_produtos"):
            AdminUI.produto_listar()
            st.subheader("Alteração de Preços")

            percentual_str: str = st.text_input("Insira o percentual de alteracao (ex: 10 para +10%, -5 para -5%): ", value=1.0) or ''
            try:
                percentual = float(percentual_str.replace(",", "."))
            except ValueError:
                percentual = 0.0

            submit: bool = st.form_submit_button("Alterar preços", type="secondary")

        if submit:
            AdminView.produto_alterar_preco_geral(percentual)
            st.success("Precos alterados com sucesso!")
            time.sleep(2)
            st.rerun()
