import sqlite3
import os
import psycopg2

# Conect to sqlite3 db
# conn = sqlite3.connect('backend/database/FUNow.db')
# cursor = conn.cursor()

database_url = os.environ['DATABASE_URL']

conn = psycopg2.connect(database_url)
cur = conn.cursor()

# Read and execute the SQL file
with open('dbSetup/FUNOW.sql', 'r') as f:
    sql_script = f.read()

cur.executemany(sql_script)
conn.commit()
conn.close()
