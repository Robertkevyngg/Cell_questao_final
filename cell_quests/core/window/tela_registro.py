from core.window.tela_base import TelaBase
from core.window.usuario import Usuario

class TelaRegistro(TelaBase):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.campoUsuario = ""
        self.campoSenha = ""
        self.botaoRegistrar = None

    def registrar(self, username, password):
        usuario = Usuario(username, password)
        return usuario.registrar(username, password)
