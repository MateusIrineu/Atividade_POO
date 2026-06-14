import streamlit as st
from Visitante.View import View as LoginView
from Visitante.Login import LoginDAO
from Admin_UI import AdminUI
from Admin.View import View as AdminView
from Cliente_UI import ClienteInterface
import time

class UI:
    @staticmethod
    def home() -> None:
        if "usuario_logado" not in st.session_state:
            st.session_state.usuario_logado = False
        if "email_logado" not in st.session_state:
            st.session_state.email_logado = None
        if "tipo_usuario" not in st.session_state:
            st.session_state.tipo_usuario = None
        if "id_cliente_logado" not in st.session_state:
            st.session_state.id_cliente_logado = None
        if "nome_cliente_logado" not in st.session_state:
            st.session_state.nome_cliente_logado = None

        if st.session_state.usuario_logado:
            if st.session_state.tipo_usuario == "admin":
                AdminUI.main()
            elif st.session_state.tipo_usuario == "entregador":
                UI.interface_entregador()
            else:
                ClienteInterface.main()
        else:
            st.header("Sistema ECommerce - Cantina Santa Clara", divider="red")
            aba1, aba2, aba3 = st.tabs(["Criar Conta Cliente", "Criar Conta Entregador", "Fazer Login"])
            with aba1:
                UI.criar_usuario()
            with aba2:
                UI.criar_entregador()
            with aba3:
                UI.validacao()

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
            AdminView.cliente_inserir(nome, email, senha, fone)
            st.success("Conta de Cliente criada com sucesso! Faça login agora.")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def criar_entregador() -> None:                           
        st.subheader("Cadastro de Entregadores")
        with st.form("form_criar_conta_entregador"):
            nome: str = st.text_input("Informe o nome completo: ")
            email: str = st.text_input("Informe o e-mail de trabalho: ")
            senha: str = st.text_input("Defina sua senha de acesso: ", type="password")
            fone: str = st.text_input("Telefone/WhatsApp: ")
            submit: bool = st.form_submit_button("Cadastrar como Entregador")
        
        if submit:
            AdminView.entregador_inserir(nome, email, senha, fone)
            st.success("Conta de Entregador criada com sucesso! Aguarde alocações após o login.")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def validacao() -> None:
        st.subheader("Forneça suas credenciais para acessar o sistema:")
        with st.form("form_logar"):
            email: str = st.text_input("Email: ")
            senha: str = st.text_input("Senha: ", type="password")
            button: bool = st.form_submit_button("Confirmar", type="secondary")

        if button:
            if (email == "admin@gmail.com") and (senha == "9999"):
                st.success("Admin logado com sucesso!")
                st.session_state.usuario_logado = True
                st.session_state.email_logado = email
                st.session_state.tipo_usuario = "admin"
                st.session_state.nome_cliente_logado = "Administrador"
                st.rerun()
            else:
                # Tentativa como Entregador
                entregador = LoginView.login_entregador(email, senha)
                if entregador:
                    st.success(f"Bem-vindo, Entregador {entregador.nome}!")
                    st.session_state.usuario_logado = True
                    st.session_state.email_logado = email
                    st.session_state.tipo_usuario = "entregador"
                    st.session_state.id_cliente_logado = entregador.id
                    st.session_state.nome_cliente_logado = entregador.nome
                    st.rerun()
                # Tentativa como Cliente tradicional
                elif LoginView.login(email, senha):
                    st.success("Login realizado com sucesso!")
                    st.session_state.usuario_logado = True
                    st.session_state.email_logado = email
                    st.session_state.tipo_usuario = "cliente"
                    st.session_state.id_cliente_logado = LoginDAO.idCliente_logado
                    st.session_state.nome_cliente_logado = LoginDAO.nome_logado
                    st.rerun()
                else:
                    st.error("Email e/ou senha incorretos!")

    @staticmethod
    def interface_entregador() -> None:
        # Interface Simples para a única função do entregador: entregar_encomenda simulado
        from Cliente.View import View as ClienteView
        st.sidebar.info(f"Entregador: {st.session_state.nome_cliente_logado}")
        if st.sidebar.button("Sair", type="primary"):
            st.session_state.usuario_logado = False
            st.session_state.email_logado = None
            st.rerun()

        st.header("Seus Pedidos para Entrega", divider="orange")
        pedidos = ClienteView.listar_pedidos_entregador(st.session_state.id_cliente_logado)
        
        if not pedidos:
            st.info("Você não possui pedidos alocados para entrega no momento.")
            return

        for p in pedidos:
            with st.container(border=True):
                st.write(f"**Pedido nº {p.id}**")
                st.write(f"Valor Total: R$ {p.total:.2f} | Status Atual: `{p.status_entrega}`")
                
                if p.status_entrega != "Entregue":
                    if st.button(f"Entregar Encomenda nº {p.id}", key=f"btn_entreg_{p.id}"):
                        ClienteView.atualizar_status_entrega(p.id, "Saiu para Entrega")
                        with st.spinner("Realizando entrega física do produto..."):
                            time.sleep(5)  # Delay acadêmico de 5 segundos requisitado
                        ClienteView.atualizar_status_entrega(p.id, "Entregue")
                        st.success(f"Entrega nº {p.id} feita com sucesso!")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.write("✅ Concluído")

UI.home()