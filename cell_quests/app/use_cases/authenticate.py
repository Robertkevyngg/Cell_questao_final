# app/use_cases/authenticate.py
from .database_operations import DatabaseOperations
from mysql.connector import Error

class Authenticate(DatabaseOperations):
    def authenticate(self, username: str, password: str) -> bool:
        QUERY = 'SELECT * FROM jogadores WHERE login = %s AND senha = %s'
        try:
            self.connect()
            self.cursor.execute(QUERY, (username, password))
            users = self.cursor.fetchall()
            return len(users) > 0
        except Error as e:
            print(f"Error: {e}")
            return False
        finally:
            self.close()
