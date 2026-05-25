import streamlit as st
from Visitante.View import View as LoginView
from Admin_UI import AdminUI
from Cliente_UI import ClienteUI

class UI:
    #CRIAÇÃO DE CONTA OU LOGIN
    @staticmethod
    def home():

        if "usuario_logado" not in st.session_state:
            st.session_state.usuario_logado = False
            st.session_state.email_logado = None
            st.session_state.tipo_usuario = None

        st.header("Sistema ECommerce - Cantina Santa Clara", divider="blue")

        if not st.session_state.usuario_logado:
            resposta: str = st.radio("Escolha a opção:", ["Criar conta", "Fazer login"])
            
            if resposta == "Criar conta":
                UI.criar_usuario()
            elif resposta == "Fazer login":
                UI.validacao()

    
    #CRIANDO USUARIO
    @staticmethod
    def criar_usuario() -> None:                           
        st.subheader("Cadastro de Clientes")
        with st.form("form_criar_conta"):
            nome: str = st.text_input("Informe o nome: ")
            email: str = st.text_input("Informe o e-mail: ")
            senha: str = st.text_input("Informe a senha: ", type="password")
            fone: str = st.text_input("Informe o fone: ")

            submit: bool = st.form_submit_button("Criar Conta")
        
        if submit:
            AdminUI.cliente_inserir(nome, email, senha, fone)
            st.success("Conta criada com sucesso! Faça login agora.")
            UI.home()

    #VALIDAÇÃO DE USUÁRIO
    @staticmethod
    def validacao() -> None:
        st.subheader("Forneça seu email e senha para logar no sistema: ")
        with st.form("form_logar"):
            email: str = st.text_input("Email: ")
            senha: str = st.text_input("Senha: ", type="password")

            button: bool = st.form_submit_button("Confirmar", type="secondary")


        if button:
            if (email == "admin@gmail.com") and (senha == "1234"):
                st.success("Admin logado com sucesso!")
                st.session_state.usuario_logado = True #estado atualizado
                AdminUI.main()

            elif LoginView.login(email, senha): #retorna o bool da função para cliente
                st.success("Login realizado com sucesso!")
                st.session_state.usuario_logado = True
                ClienteUI.cliente_main()

            else:
                st.error("Email e/ou senha incorretos!")

UI.home()