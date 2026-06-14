from .Login import Login, LoginDAO
from Admin.Cliente import Cliente, ClienteDAO
from Admin.Entregador import Entregador, EntregadorDAO

class View:
    #CRIAR CONTA DE USUARIO
    @staticmethod
    def criar_conta(nome, email, senha, fone):
        c = Cliente(0, nome, email, senha, fone)
        ClienteDAO.inserir(c)
    
    #LOGANDO NO SISTEMA
    @staticmethod
    def login(email, senha) -> bool:
        logado = LoginDAO.logado(email, senha)
        return logado
    # Método para verificar login de entregadores
    from Admin.Entregador import EntregadorDAO

    @staticmethod
    def login_entregador(email, senha):
        EntregadorDAO.abrir()
        for e in EntregadorDAO.objetos:
            if e.email == email and e.senha == senha:
                return e
        return None