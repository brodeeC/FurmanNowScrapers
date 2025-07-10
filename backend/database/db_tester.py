import sqlite3



def main():
    conn = sqlite3.connect('backend/database/FUNow.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM DHmenu')
    items = cursor.fetchall()
    for item in items:
        print(item)
    
    conn.close()

if __name__ == '__main__':
    main()