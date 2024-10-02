import sys
import os

# Adiciona o caminho do diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..')))

from core.window.tela_login import TelaLogin
from core.window.tela_registro import TelaRegistro
from core.window.tela_questao import TelaQuestao
from core.window.tela_ranking import TelaRanking
from core.window.tela_pontuacao import TelaPontuacao

class Aplicacao:
    def __init__(self):
        self.tela_login = TelaLogin(800, 600)
        self.tela_registro = TelaRegistro(800, 600)
        self.tela_questao = TelaQuestao(800, 600)
        self.tela_ranking = TelaRanking(800, 600)
        self.tela_pontuacao = TelaPontuacao(800, 600)

    def iniciar(self):
        # Exemplo de fluxo da aplicação
        self.tela_login.mostrar()
        autenticado = self.tela_login.autenticar("usuario", "senha")
        if autenticado:
            self.tela_questao.mostrar()
        else:
            self.tela_registro.mostrar()
            registrado = self.tela_registro.registrar("novo_usuario", "nova_senha")
            if registrado:
                self.tela_login.mostrar()

if __name__ == "__main__":
    app = Aplicacao()
    app.iniciar()
