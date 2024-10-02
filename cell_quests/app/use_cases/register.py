# app/use_cases/register.py
from aifc import Error
from .database_operations import DatabaseOperations

class Register(DatabaseOperations):
    def register(self, username: str, password: str) -> bool:
        QUERY = 'INSERT INTO jogadores (login, senha) VALUES (%s, %s)'
        try:
            self.connect()
            self.cursor.execute(QUERY, (username, password))
            self.conn.commit()
            return True
        except Error as e:
            print(f"Error: {e}")
            return False
        finally:
            self.close()
