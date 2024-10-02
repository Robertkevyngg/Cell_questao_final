class Usuario:
    def __init__(self, usuario, senha, pontuacao=0):
        self.usuario = usuario
        self.senha = senha
        self.pontuacao = pontuacao

    def autenticarUsuario(self, username, password):
        return self.usuario == username and self.senha == password

    def registrar(self, username, password):
        # Lógica para registrar um novo usuário
        pass
