import sqlite3

DB_FILE_PATH = 'data/crm.db'


class Db:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE_PATH)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def execute(self, query, data=None):
        if data is not None:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)

    def commit(self):
        self.conn.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()
