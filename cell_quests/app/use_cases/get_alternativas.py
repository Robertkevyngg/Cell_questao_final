from mysql.connector import Error  # Import specific Error
from .database_operations import DatabaseOperations

class GetAlternatives(DatabaseOperations):
    def get_alternatives(self, question_id: int) -> dict:
        QUERY = (
            "SELECT opcao_id, questao_id, texto_opcao, letra_opcao "
            "FROM opcoes_resposta "
            "WHERE questao_id = %s"
        )
        try:
            self.connect()
            self.cursor.execute(QUERY, (question_id,))
            alternatives: list[tuple] = self.cursor.fetchall()  # Type hint

            formatted_response: dict = {}  # Type hint
            for _, _, text, letter in alternatives:
                formatted_response[str(letter)] = text

            return formatted_response
        except Error as e:
            print(f"Database Error: {e}")  # More specific error handling
            return {}
        finally:
            self.close()