from mysql.connector import Error
from .database_operations import DatabaseOperations

class GetQuestions(DatabaseOperations):
    def get_questions(self):
        QUERY = (
            "SELECT q.questao_id, q.enunciado, o.letra_opcao as resposta "
            "FROM questoes as q "
            "INNER JOIN opcoes_resposta as o ON q.questao_id = o.questao_id "
            "INNER JOIN respostas_corretas as r ON r.questao_id = q.questao_id AND r.opcao_id = o.opcao_id"
        )
        try:
            self.connect()
            self.cursor.execute(QUERY)
            questions = []
            for (questao_id, enunciado, resposta) in self.cursor.fetchall():
                questions.append({
                    'questao_id': questao_id,
                    'enunciado': enunciado,
                    'resposta': resposta
                })
            return questions
        except Error as e:
            print(f"Database Error: {e}")  # More specific error handling
            return []
        finally:
            self.close()