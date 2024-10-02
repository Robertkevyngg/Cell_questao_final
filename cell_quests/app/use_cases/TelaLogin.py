class TelaLogin(TelaBase):
    def __init__(self, largura: int, altura: int):
        super().__init__(largura, altura)
        self.campoUsuario = None
        self.campoSenha = None
        self.botaoLogin = None
    
    def fazer_login(self, username: str, password: str):
        # Implementar lógica de login
        pass
