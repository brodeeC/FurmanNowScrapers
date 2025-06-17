import sqlite3
import re
from datetime import datetime

class SQLiteCursorWrapper:
    def __init__(self, cursor):
        self.cursor = cursor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()

    def execute(self, query, params=()):
        try:
            # Convert MySQL query to SQLite format
            converted_query = self._convert_query(query)
            # Execute with converted query and original params
            return self.cursor.execute(converted_query, params)
        except sqlite3.Error as e:
            print(f"SQL Error: {e}\nQuery: {converted_query}\nParams: {params}")
            raise

    def _convert_query(self, query):
        """Convert MySQL-style queries to SQLite-compatible format"""
        # Remove all backticks
        query = query.replace('`', '')
        
        # Replace %s with ?
        query = query.replace('%s', '?')
        
        # Fix INSERT statements (don't touch the INTO part)
        query = re.sub(r'INSERT\s+(INTO\s+)?([^\s(]+)', 
                    lambda m: f"INSERT INTO {m.group(2)}", 
                    query, flags=re.IGNORECASE)
        return query

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def __getattr__(self, name):
        return getattr(self.cursor, name)

class SQLiteConnectionWrapper:
    def __init__(self, path="backend/database/FUNow.db"):
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