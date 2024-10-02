# app/use_cases/database_operations.py
from core.database.connector import establish_connection
from mysql.connector import Error

class DatabaseOperations:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = establish_connection()
        if self.conn and self.conn.is_connected():
            self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
