import sqlite3
import re

# Wrapper class to emulate pymysql on sqlite database
class SQLiteCursorWrapper:
    def __init__(self, cursor):
        self.cursor = cursor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.cursor.close()

    def execute(self, query, params=()):
        # Replace MySQL-style placeholders and backticks
        query = re.sub(r'`([^`]+)`', r'\1', query)     # remove backticks
        query = query.replace('%s', '?')               # replace placeholders
        return self.cursor.execute(query, params)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def __getattr__(self, name):
        return getattr(self.cursor, name)


class SQLiteConnectionWrapper:
    def __init__(self, path="local_test.db"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row

    def cursor(self):
        return SQLiteCursorWrapper(self.conn.cursor())

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.conn.close()

    def __getattr__(self, name):
        return getattr(self.conn, name)
