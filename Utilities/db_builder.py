import sqlite3
import requests

url = "https://cs.furman.edu/~csdaemon/FUNow/buildingGet.php"
url_hours = 'https://cs.furman.edu/~csdaemon/FUNow/hoursGet.php'

def sql_escape(value):
    if value is None:
        return "NULL"
    if isinstance(value, str):
        # Escape single quotes for SQL
        return "'" + value.replace("'", "''") + "'"
    return str(value)

def connect_to_local_db(db_path="local_test.db"):
    connection = sqlite3.connect(db_path)
    return connection

def create_tables(db_path="local_test.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS buildingHours;")
    cursor.execute("DROP TABLE IF EXISTS buildingLocations;")

    cursor.execute("""
    CREATE TABLE buildingHours (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        buildingID INTEGER NOT NULL,
        day TEXT NOT NULL,
        dayorder INTEGER NOT NULL, 
        Start TIME,
        End TIME,
        lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (buildingID) REFERENCES buildingLocations(id)
    );
""")

    cursor.execute("""
        CREATE TABLE buildingLocations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        buildingID INTEGER UNIQUE NOT NULL,
        name TEXT NOT NULL,
        nickname TEXT,
        category TEXT,
        hasHours INTEGER DEFAULT 0,
        website TEXT,
        location TEXT,
        latitude REAL,
        longitude REAL,
        polyline TEXT,
        description TEXT,
        frequency INTEGER DEFAULT 0,
        last_updated DATETIME
    );
    """)
    conn.commit()
    conn.close()

def main():
    create_tables()
    conn = sqlite3.connect('local_test.db')
    cursor = conn.cursor()

    # Fetch JSON data
    response = requests.get(url, verify=False)
    data = response.json()
    results = data.get("results", [])

    # Insert buildings
    for b in results:
        cursor.execute("""
            INSERT INTO buildingLocations (
                buildingID, name, nickname, category, hasHours, website, location,
                latitude, longitude, polyline, description, frequency, last_updated
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            b.get("buildingID"),
            b.get("name"),
            b.get("nickname"),
            b.get("category"),
            b.get("hasHours"),
            b.get("website"),
            b.get("location"),
            b.get("latitude"),
            b.get("longitude"),
            b.get("polyline"),
            b.get("description"),
            b.get("frequency"),
            b.get("last_updated"),
        ))

    conn.commit()

    response = requests.get(url_hours, verify=False)
    data = response.json()
    results = data.get("results", [])

    for h in results:
        cursor.execute("""
            INSERT INTO buildingHours (
                id, buildingID, day, dayorder, Start, End, lastUpdated
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            h.get("id"),
            h.get("buildingID"),
            h.get("day"),
            h.get("dayorder"),
            h.get("Start"),
            h.get("End"),
            h.get("lastUpdated"),
        ))

    conn.commit()
    
    # Print all buildings with their IDs
    cursor.execute("SELECT buildingID, name FROM buildingLocations")
    buildings = cursor.fetchall()
    print("Buildings in database:")
    for b_id, name in buildings:
        print(f"ID: {b_id}, Name: {name}")
    
    conn.close()

if __name__ == '__main__':
    main()