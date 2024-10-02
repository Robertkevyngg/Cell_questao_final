from core.window.tela_base import TelaBase
from core.window.usuario import Usuario

class TelaLogin(TelaBase):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.campoUsuario = ""
        self.campoSenha = ""
        self.botaoLogin = None

    def autenticar(self, username, password):
        usuario = Usuario(username, password)
        return usuario.autenticarUsuario(username, password)
