from core.window.tela_base import TelaBase
from core.window.questao import Questao
from core.window.professor import Professor

class TelaQuestao(TelaBase):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.caixaEnunciado = ""
        self.caixaCorpo = ""
        self.caixaAlternativas = ""

    def adicionar_questao(self, enunciado, numero_alternativas):
        professor = Professor('professor', 'senha')
        questao = Questao(enunciado, numero_alternativas)
        professor.adicionarQuestao(questao)
