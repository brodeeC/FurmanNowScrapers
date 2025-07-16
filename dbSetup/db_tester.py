import sqlite3
import psycopg2



def main():
    database_url = 'postgres://fly-user:aKU5MULCzWL1ctLggz8AOF1F@direct.q49ypo4wyxdr17ln.flympg.net/fly-db'

    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM information_schema.tables')
    items = cursor.fetchall()
    for item in items:
        print(item)
    
    conn.close()

if __name__ == '__main__':
    main()