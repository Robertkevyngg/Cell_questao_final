# app/use_cases/get_scoreboard.py
from aifc import Error
from .database_operations import DatabaseOperations

class GetScoreboard(DatabaseOperations):
    def get_scoreboard(self):
        QUERY = "SELECT * FROM pontuacoes ORDER BY pontuacao DESC LIMIT 10"
        try:
            self.connect()
            self.cursor.execute(QUERY)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            self.close()
