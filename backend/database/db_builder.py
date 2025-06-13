import sqlite3
import requests

# URLs for buildingLocations and buildingHours data
url = "https://cs.furman.edu/~csdaemon/FUNow/buildingGet.php"
# url_hours = 'https://cs.furman.edu/~csdaemon/FUNow/hoursGet.php'

# Creates buildingHours and buildingLocations tables in database
def create_building_hrs(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS buildingHours;")

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

    conn.commit()
    conn.close()

def create_building_locs(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS buildingLocations;")

    # Create the athletics table
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

def create_athletics_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS athletics;")

    # Create the athletics table
    cursor.execute("""
    CREATE TABLE athletics (
        id INTEGER PRIMARY KEY,
        eventdate TEXT NOT NULL,
        time TEXT,
        conference TEXT,
        location_indicator TEXT,
        location TEXT,
        sportTitle TEXT,
        sportShort TEXT,
        opponent TEXT,
        noplayText TEXT,
        resultStatus TEXT,
        resultUs TEXT,
        resultThem TEXT,
        prescore_info TEXT,
        postscore_info TEXT,
        url TEXT,
        lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()

def create_clp_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS clp;")

    # Create the clp table
    cursor.execute("""
    CREATE TABLE clp (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        location TEXT,
        date TEXT NOT NULL,
        start TIME,
        end TIME,
        organization TEXT,
        eventType TEXT,
        lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()

def create_contacts_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS contacts;")

    # Create the contacts table
    cursor.execute("""
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY,
        buildingID INTEGER NOT NULL,
        room TEXT,
        name TEXT NOT NULL,
        number TEXT NOT NULL,
        lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        priorityLevel INTEGER
    );
    """)

    conn.commit()
    conn.close()

def create_dhmenu_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS dhMenu;")

    # Create the dhMenu table
    cursor.execute("""
    CREATE TABLE dhMenu (
        id INTEGER,
        meal TEXT NOT NULL,
        station TEXT NOT NULL,
        itemName TEXT NOT NULL
    );
    """)

    conn.commit()
    conn.close()

def create_healthsafety_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS healthSafety;")

    # Create the healthSafety table
    cursor.execute("""
    CREATE TABLE healthSafety (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        shortName TEXT,
        content TEXT NOT NULL,
        type TEXT NOT NULL,
        icon TEXT,
        priority INTEGER
    );
    """)

    conn.commit()
    conn.close()

def create_importantdate_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS importantDate;")

    # Create the importantDate table
    cursor.execute("""
    CREATE TABLE importantDate (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        date TEXT NOT NULL,
        startTime TIME,
        endTime TIME,
        category TEXT,
        description TEXT,
        term TEXT,
        lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()

def create_importantlinks_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS importantLinks;")

    # Create the importantLinks table
    cursor.execute("""
    CREATE TABLE importantLinks (
        id INTEGER PRIMARY KEY,
        priority INTEGER,
        name TEXT NOT NULL,
        content TEXT NOT NULL,
        type TEXT NOT NULL
    );
    """)

    conn.commit()
    conn.close()

def create_newscontent_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS newsContent;")

    # Create the newsContent table
    cursor.execute("""
    CREATE TABLE newsContent (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        description TEXT,
        media TEXT,
        linktocontent TEXT NOT NULL,
        publisherID INTEGER,
        section TEXT,
        publishdate DATETIME,
        imagelink TEXT
    );
    """)

    conn.commit()
    conn.close()

def create_newspublishers_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS newsPublishers;")

    # Create the newsPublishers table
    cursor.execute("""
    CREATE TABLE newsPublishers (
        publisherID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        link TEXT NOT NULL,
        image TEXT,
        studentRun INTEGER NOT NULL CHECK (studentRun IN (0, 1))
    );
    """)

    conn.commit()
    conn.close()

def create_shuttles_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS shuttles;")

    # Create the shuttles table
    cursor.execute("""
    CREATE TABLE shuttles (
        id INTEGER PRIMARY KEY,
        vehicle TEXT NOT NULL,
        latitude REAL,
        longitude REAL,
        speed REAL,
        direction TEXT,
        nextStopDistance REAL,
        updated DATETIME NOT NULL,
        nextStopID INTEGER
    );
    """)

    conn.commit()
    conn.close()

def create_vehicleNames_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS vehicleNames;")

    cursor.execute("""
    CREATE TABLE vehicleNames (
        vehicleIndex INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        shortName TEXT,
        serviceTimes TEXT,
        locations TEXT,
        colorRed REAL,
        colorGreen REAL,
        colorBlue REAL,
        iconName TEXT,
        routePolyline TEXT,
        website TEXT,
        color TEXT,
        averageSpeed INTEGER,
        averageStopSeconds INTEGER,
        message TEXT
    );
    """)

    conn.commit()
    conn.close()
    
def create_vehicleNames_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS shuttleStops;")

    cursor.execute("""
        CREATE TABLE shuttleStops (
            lineID INTEGER NOT NULL,
            stopOrderID INTEGER NOT NULL,
            distFromStart REAL NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            stopName TEXT NOT NULL,
            distFromVehicle REAL,
            updated TEXT NOT NULL,
            vehicleStopsUntil TEXT,
            PRIMARY KEY (lineID, stopOrderID)
        );
    """)

    conn.commit()
    conn.close()

import sqlite3

def create_weather_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS weather;")

    cursor.execute("""
        CREATE TABLE weather (
            id INTEGER PRIMARY KEY,
            day TEXT NOT NULL,
            start TEXT NOT NULL,
            end TEXT NOT NULL,
            isDayTime INTEGER NOT NULL,
            tempCurrent INTEGER,
            tempHi INTEGER,
            tempLo INTEGER,
            unit TEXT,
            precipitationPercent INTEGER,
            windSpeed TEXT,
            windDirection TEXT,
            shortForecast TEXT,
            detailedForecast TEXT,
            alert TEXT,
            emoji TEXT
        );
    """)

    conn.commit()
    conn.close()

def create_images_table(db_path="FUNow.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS images;")

    cursor.execute("""
        CREATE TABLE images (
            generated TEXT NOT NULL,
            link TEXT NOT NULL PRIMARY KEY
        );
    """)

    conn.commit()
    conn.close()

def create_tables(path='FUNow.db'):
    create_building_hrs(path)
    create_building_locs(path)
    create_athletics_table(path)
    create_clp_table(path)
    create_contacts_table(path)
    create_dhmenu_table(path)
    create_healthsafety_table(path)
    create_images_table(path)
    create_importantdate_table(path)
    create_importantlinks_table(path)
    create_newscontent_table(path)
    create_newspublishers_table(path)
    create_shuttles_table(path)
    create_shuttles_table(path)
    create_vehicleNames_table(path)
    create_weather_table(path)


# Inserts data found from urls in db
def main():
    create_tables('backend/database/FUNow.db')
    conn = sqlite3.connect('backend/database/FUNow.db')
    cursor = conn.cursor()

    # # Fetch JSON data
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

    # response = requests.get(url_hours, verify=False)
    # data = response.json()
    # results = data.get("results", [])

    # for h in results:
    #     cursor.execute("""
    #         INSERT INTO buildingHours (
    #             id, buildingID, day, dayorder, Start, End, lastUpdated
    #         ) VALUES (?, ?, ?, ?, ?, ?, ?)
    #     """, (
    #         h.get("id"),
    #         h.get("buildingID"),
    #         h.get("day"),
    #         h.get("dayorder"),
    #         h.get("Start"),
    #         h.get("End"),
    #         h.get("lastUpdated"),
    #     ))

    # conn.commit()
    
    # # Print all buildings with their IDs
    cursor.execute("SELECT buildingID, name FROM buildingLocations")
    buildings = cursor.fetchall()
    print("Buildings in database:")
    for b_id, name in buildings:
        print(f"ID: {b_id}, Name: {name}")
    
    conn.close()

if __name__ == '__main__':
    main()