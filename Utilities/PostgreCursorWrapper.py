import psycopg2
from psycopg2.extras import DictCursor
import os
import re
from contextlib import contextmanager

class PostgresConnection:
    def __init__(self):
        self.conn = self._connect()
    
    def _connect(self):
        """Establish connection with automatic configuration"""
        try:
            conn = psycopg2.connect(
                dsn=os.environ['DATABASE_URL'],
                cursor_factory=DictCursor,
                connect_timeout=2,
                application_name="FUNOW"
            )
            conn.autocommit = False
            with conn.cursor() as cursor:
                cursor.execute("SET TIME ZONE 'UTC';")
            return conn
        except psycopg2.Error as e:
            print(f"Connection failed: {e}")
            raise
    
    def _convert_query(self, query):
        """Convert MySQL-style queries to PostgreSQL format"""
        # Replace backticks with PostgreSQL's double quotes
        query = query.replace('`', '"')
        
        # Replace MySQL's %s placeholders if they exist
        if '%s' in query and not any(w in query.upper() for w in ['LIKE', 'ILIKE']):
            query = query.replace('%s', '%s')  # PostgreSQL also uses %s
        
        # Fix INSERT statements if needed
        query = re.sub(r'INSERT\s+(IGNORE\s+)?INTO\s+', 'INSERT INTO ', query, flags=re.IGNORECASE)
        
        return query

    @contextmanager
    def cursor(self):
        """Context manager for cursor handling"""
        cursor = self.conn.cursor()
        try:
            yield cursor
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(f"Query failed: {e}")
            raise
        finally:
            cursor.close()

    def execute(self, query, params=None, skip_conversion=False):
        converted_query = self._convert_query(query) if not skip_conversion else query
        with self.cursor() as cursor:
            cursor.execute(converted_query, params or ())
            if cursor.description:  
                return cursor.fetchall()

    def close(self):
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()