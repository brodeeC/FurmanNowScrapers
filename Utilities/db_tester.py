import sqlite3


def connect_to_local_db(db_path="local_test.db"):
    connection = sqlite3.connect(db_path)
    return connection

# Currently contains 49,978 lines in buildingHours.
def main():
    conn = sqlite3.connect('local_test.db')
    cursor = conn.cursor()

    cursor.execute("SELECT buildingID, day, Start, End FROM buildingHours")
    buildings = cursor.fetchall()
    print("Buildings in database:")
    for buildingID, day, Start, End in buildings:
        print(f"ID: {buildingID}, Day: {day}, Start: {Start}, End: {End}")

    cursor.execute("SELECT COUNT(*) FROM buildingHours")
    print(cursor.fetchone())

    conn.close()

if __name__ == '__main__':
    main()