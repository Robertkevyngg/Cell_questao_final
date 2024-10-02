from core.window.tela_base import TelaBase

class TelaPontuacao(TelaBase):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.campoPontuacao = ""
