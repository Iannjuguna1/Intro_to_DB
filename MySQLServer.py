# MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (adjust host, user, password)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # <-- Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection properly
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            #print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()

