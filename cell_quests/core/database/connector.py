# core/database/connector.py
import mysql.connector
from mysql.connector import Error

def establish_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='quiz_citologia',
            user='root',
            password='1234'
        )
        if conn.is_connected():
            print('Connected to MySQL database')
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None
