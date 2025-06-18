import sqlite3

# Connect to your SQLite database (or create it)
conn = sqlite3.connect('backend/database/FUNow.db')
cursor = conn.cursor()

# Read and execute the SQL file
with open('backend/database/FUNow.sql', 'r') as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()
