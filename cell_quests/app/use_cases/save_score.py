# app/use_cases/save_score.py
from aifc import Error
from .database_operations import DatabaseOperations

class SaveScore(DatabaseOperations):
    def save_score(self, current_player_id: int, score: int):
        QUERY = "INSERT INTO pontuacoes (jogador_id, pontuacao) VALUES (%s, %s)"
        try:
            self.connect()
            self.cursor.execute(QUERY, (current_player_id, score))
            self.conn.commit()  # Commit the transaction
            print("Score saved successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            self.close()
