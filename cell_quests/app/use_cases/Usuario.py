class Usuario:
    def __init__(self, usuario: str, senha: str, pontuacao: int):
        self.usuario = usuario
        self.senha = senha
        self.pontuacao = pontuacao
    
    def autenticar(self, username: str, password: str) -> bool:
        # Implementar lógica de autenticação
        pass
    
    def registrar(self, username: str, password: str) -> bool:
        # Implementar lógica de registro
        pass
