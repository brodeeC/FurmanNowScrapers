import sqlite3

# Currently contains 49,980 lines in buildingHours.
def main():
    conn = sqlite3.connect('backend/database/FUNow.db')
    cursor = conn.cursor()

    cursor.execute("SELECT buildingID, day, Start, End FROM buildingHours")
    buildings = cursor.fetchall()
    print("Buildings in database:")
    for buildingID, day, Start, End in buildings:
        print(f"ID: {buildingID}, Day: {day}, Start: {Start}, End: {End}")

    cursor.execute("SELECT COUNT(*) FROM buildingHours")
    print(cursor.fetchone())
    cursor.execute("""
        SELECT buildingID, COUNT(*) AS num_entries
        FROM buildingHours
        GROUP BY buildingID
        ORDER BY num_entries DESC;
    """)
    tuples = cursor.fetchall()
    for buildings in tuples:
        building_id, entries = buildings[0], buildings[1]
        cursor.execute(f"SELECT name FROM buildingLocations WHERE buildingID = {building_id};")
        res = cursor.fetchone()
        name = res[0] if res else 'Unknown'
        print(f'Name: {name} - entries: {entries}')
    

    conn.close()

if __name__ == '__main__':
    main()