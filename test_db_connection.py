import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='quiz_citologia',
            user='root',
            password='1234'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

conn = create_connection()
if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
    cursor.close()
    conn.close()
