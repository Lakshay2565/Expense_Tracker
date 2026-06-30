import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("expense.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                description TEXT,
                amount REAL
            )
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()