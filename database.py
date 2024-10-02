# database.py
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def establish_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def show_databases():
    conn = establish_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        for db in cursor:
            print(db)
        cursor.close()
        conn.close()

if __name__ == "__main__":
    show_databases()
